from FactorioCalcBase.data.recipe_dict import recipe_dict
from recipe_class import RecipeClass
from oil_processing import FactorioOilReqToRecipe


class DependencyTracker:
    def __init__(self, recipe_name: str, amount=1, resource_consumption_rate_dict=None):
        self.name = recipe_name
        self.amount = amount
        self.recipe_obj = RecipeClass(recipe_name)
        if resource_consumption_rate_dict is None:
            resource_consumption_rate_dict = {}
        self.resource_consumption_rate_dict = resource_consumption_rate_dict
        self.cannot_process_item_dict = {}
        self.item_needed_dict = self.recipe_obj.ingredients
        self.results = self.recipe_obj.results
        self.oil_obj = None
        self.initial_total_recipe_req_dict = self.get_initial_recipe_req_dict()
        self.initial_total_item_req_dict = self.get_initial_item_req_dict()

    def get_initial_recipe_req_dict(self):
        self.recipe_obj.amount = self.amount
        obj_search_queue = [self.recipe_obj]
        item_needed_queue = []
        cannot_process_item_dict = {}
        total_recipe_needed_dict = {self.recipe_obj.name: self.recipe_obj.amount}
        while obj_search_queue != []:
            current = obj_search_queue[0]
            if current.ingredients != '':
                for key in current.ingredients.keys():
                    resource_consumption_ratio = self.resource_consumption_rate_dict.get(key)
                    if resource_consumption_ratio is None:
                        resource_consumption_ratio = 1
                    to_append = [key, current.ingredients[key] * current.amount * resource_consumption_ratio]
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
                    if cannot_process_item_dict.get(item_needed_queue[0][0]) is None:
                        cannot_process_item_dict[item_needed_queue[0][0]] = 0
                    cannot_process_item_dict[item_needed_queue[0][0]] += item_needed_queue[0][1]
                item_needed_queue.pop(0)
            obj_search_queue.pop(0)
        self.cannot_process_item_dict = cannot_process_item_dict
        self.oil_obj = FactorioOilReqToRecipe(self.cannot_process_item_dict, self.resource_consumption_rate_dict)

        return total_recipe_needed_dict

    def cpid_handle(self, general_dict: dict, r_or_i: str):
        if self.cannot_process_item_dict == {}:
            pass
        else:
            oil_obj = self.oil_obj
            oil_recipe_dict = oil_obj.get_recipe_needed()
            oil_item_dict = oil_obj.get_item_needed()
            new_dict = {
                'recipe': oil_recipe_dict,
                'item': oil_item_dict
            }
            roi = None
            if r_or_i == 'r':
                roi = 'recipe'
            elif r_or_i == 'i':
                roi = 'item'

            if roi is not None:
                to_return_dict = {
                    'general_' + roi: general_dict,
                    'oil_' + roi: new_dict[roi]
                }
                return to_return_dict

    # @staticmethod
    # def dict_add(main: dict, to_add: dict):
    #     for key in list(to_add.keys()):
    #         if main.get(key) is None:
    #             main[key] = 0
    #         main[key] += to_add[key]

    def get_initial_item_req_dict(self):
        new_dict = {}
        total_needed_recipe = self.initial_total_recipe_req_dict
        for key in total_needed_recipe.keys():
            to_add = recipe_dict[key]['results']
            for keykey in to_add.keys():
                if keykey not in new_dict:
                    new_dict[keykey] = 0
                new_dict[keykey] += to_add[keykey] * total_needed_recipe[key]

        # merged_dict = self.cpid_handle(general_dict=new_dict, r_or_i='i')

        return new_dict

    @staticmethod
    def find_recipe(needed_list):
        item_name = needed_list[0]
        item_amount = needed_list[1]

        recipe_name = ''
        recipe_amount = 0
        trc = RecipeClass(item_name)
        if item_name in ['petroleum-gas', 'light-oil', 'heavy-oil', 'solid-fuel']:
            return -1
        elif item_name == 'solid-fuel':  # TODO solid-fuel, 우라늄 관련 레시피 반영 필요
            recipe_name = 'solid-fuel-from-light-oil'
            recipe_amount = item_amount / trc.get_results_count()

        elif trc.is_name_results_match():
            recipe_name = item_name
            recipe_amount = item_amount / trc.get_results_count()

        if recipe_name != '' and recipe_amount != 0:
            return [recipe_name, recipe_amount]


class DependencyDictMerged:
    def __init__(self, recipe_name: str, amount=1, resource_consumption_rate_dict=None):
        teclass = DependencyTracker(recipe_name, amount, resource_consumption_rate_dict)

        self.total_recipe_req_dict = teclass.initial_total_recipe_req_dict
        self.total_item_req_dict = teclass.initial_total_item_req_dict

        self.merged_recipe_dict = teclass.cpid_handle(self.total_recipe_req_dict, 'r')
        self.merged_item_dict = teclass.cpid_handle(self.total_item_req_dict, 'i')
        self.rec_gen = self.total_recipe_req_dict
        self.rec_oil = self.merged_recipe_dict['oil_recipe']
        self.itm_gen = self.total_item_req_dict
        self.itm_oil = self.merged_item_dict['oil_item']
        self.merged_oil_dict = {
            'oil_recipe': self.rec_oil,
            'oil_item': self.itm_oil
        }
        self.merged_gen_dict = {
            'general_recipe': self.rec_gen,
            'general_item': self.itm_gen
        }
