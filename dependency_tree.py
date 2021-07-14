from data.recipe_dict import recipe_dict
from recipe_class import RecipeClass
from oil_processing import FactorioOilNeedToRecipe


class RecipeDependency:
    def __init__(self, recipe_name: str, resource_consumption_rate_dict = None):
        self.name = recipe_name
        self.recipe_obj = RecipeClass(recipe_name)
        if resource_consumption_rate_dict is None:
            resource_consumption_rate_dict = {}
        self.resource_consumption_rate_dict = resource_consumption_rate_dict

        self.item_needed = self.recipe_obj.ingredients
        self.results = self.recipe_obj.results
        # self.recipe_needed = self.get_total_item_needed()

    def get_total_recipe_req_dict(self, self_amount=1):
        self.recipe_obj.amount = self_amount
        obj_search_queue = [self.recipe_obj]
        item_needed_queue = []
        cannot_process_dict = {}
        total_recipe_needed_dict = {self.recipe_obj.name: self.recipe_obj.amount}
        while obj_search_queue != []:
            current = obj_search_queue[0]
            if current.ingredients != '':
                for key in current.ingredients.keys():
                    to_append = [key, current.ingredients[key]*current.amount]
                    item_needed_queue.append(to_append)
            while item_needed_queue != []:
                if self.find_recipe(item_needed_queue[0]) != -1:
                    returned_recipe_list = self.find_recipe(item_needed_queue[0])
                    # returned_recipe_list, [0]: name, [1]: amount
                    if total_recipe_needed_dict.get(returned_recipe_list[0]) is None:
                        total_recipe_needed_dict[returned_recipe_list[0]] = 0
                    total_recipe_needed_dict[returned_recipe_list[0]] += returned_recipe_list[1]
                    new_obj = RecipeClass(returned_recipe_list[0])
                    new_obj.amount = returned_recipe_list[1]
                    obj_search_queue.append(new_obj)
                else:
                    # item_needed_queue[0][b], 0: index, b:0: item name, b:1: item amount
                    if cannot_process_dict.get(item_needed_queue[0][0]) is None:
                        cannot_process_dict[item_needed_queue[0][0]] = 0
                    cannot_process_dict[item_needed_queue[0][0]] += item_needed_queue[0][1]
                item_needed_queue.pop(0)
            obj_search_queue.pop(0)
        print(cannot_process_dict)
        self.handle_cpd(cannot_process_dict)
        return total_recipe_needed_dict

    def handle_cpd(self, cpd):
        new_obj = FactorioOilNeedToRecipe(cpd,self.resource_consumption_rate_dict)
        to_return_dict = new_obj.get_recipe_needed()
        oil_recipe_needed_ingredient_dict = {}
        print(to_return_dict)

    def total_needed_item(self):
        new_dict={}
        total_needed_recipe = self.get_total_recipe_req_dict()
        for key in total_needed_recipe.keys():
            to_add = recipe_dict[key]['results']
            for keykey in to_add.keys():
                if keykey not in new_dict:
                    new_dict[keykey] = 0
                new_dict[keykey] += to_add[keykey]*total_needed_recipe[key]
        return new_dict

    def find_recipe(self, needed_list):
        item_name = needed_list[0]
        item_amount = needed_list[1]

        recipe_name = ''
        recipe_amount = 0
        trc = RecipeClass(item_name)
        if trc.name in ['petroleum-gas', 'light-oil', 'heavy-oil', 'solid-fuel']:
            return -1
        elif trc.is_name_results_match():
            recipe_name = item_name
            recipe_amount = item_amount / trc.get_results_count()
        if recipe_name != '' and recipe_amount != 0:
            return [recipe_name, recipe_amount]
