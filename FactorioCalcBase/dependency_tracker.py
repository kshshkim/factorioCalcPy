from data.binary import recipe_dict
from recipe_class import RecipeClass
from oil_processing import OilProcessor
from collections import Counter


class DependencyTracker:
    def __init__(self, recipe_name: str, amount=1, extra_product_rate_dict=None):
        self.name = recipe_name
        self.amount = amount
        self.recipe_obj = RecipeClass(recipe_name)
        if extra_product_rate_dict is None:
            extra_product_rate_dict = {}
        self.extra_product_rate_dict = extra_product_rate_dict
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
                    to_append = [key, current.ingredients[key] * current.amount]
                    item_needed_queue.append(to_append)
            while item_needed_queue != []:  # [0] = current, [][0] = name [][1] = amount
                if self.find_recipe(item_needed_queue[0]) != -1:
                    returned_recipe_list = self.find_recipe(item_needed_queue[0])
                    # returned_recipe_list, [0]: name, [1]: amount
                    recipe_name = returned_recipe_list[0]
                    recipe_amount = returned_recipe_list[1]
                    if total_recipe_needed_dict.get(recipe_name) is None:
                        total_recipe_needed_dict[recipe_name] = 0
                    total_recipe_needed_dict[recipe_name] += recipe_amount
                    new_obj = RecipeClass(recipe_name)
                    new_obj.amount = recipe_amount
                    obj_search_queue.append(new_obj)
                else:
                    # item_needed_queue[0][b], 0: index, b:0: item name, b:1: item amount
                    if cannot_process_item_dict.get(item_needed_queue[0][0]) is None:
                        cannot_process_item_dict[item_needed_queue[0][0]] = 0
                    cannot_process_item_dict[item_needed_queue[0][0]] += item_needed_queue[0][1]
                item_needed_queue.pop(0)
            obj_search_queue.pop(0)
        self.cannot_process_item_dict = cannot_process_item_dict

        return total_recipe_needed_dict

    def get_initial_item_req_dict(self):
        new_dict = {}
        total_needed_recipe = self.initial_total_recipe_req_dict
        for key in total_needed_recipe.keys():
            to_add = recipe_dict[key]['results']
            for keykey in to_add.keys():
                if keykey not in new_dict:
                    new_dict[keykey] = 0
                new_dict[keykey] += to_add[keykey] * total_needed_recipe[key]
        return new_dict

    def find_recipe(self, needed_list):
        item_name = needed_list[0]
        item_amount = needed_list[1]

        recipe_name = ''
        trc = RecipeClass(item_name)
        # name_results_match 가 아니면 따로 처리

        if trc.is_name_results_match():
            recipe_name = item_name
        elif item_name in ['petroleum-gas', 'light-oil', 'heavy-oil', 'solid-fuel']:
            return -1
        elif item_name == 'solid-fuel':  # TODO solid-fuel, 우라늄 관련 레시피 반영 필요
            recipe_name = 'solid-fuel-from-light-oil'

        extra_product_rate = self.extra_product_rate_dict.get(recipe_name)
        if extra_product_rate is None:
            extra_product_rate = 1

        recipe_amount = item_amount / (trc.get_results_count()*extra_product_rate)
        if recipe_name != '' and recipe_amount != 0:
            return [recipe_name, recipe_amount]


class DependencyDictMerged:
    # TODO 하드코딩 정리
    def __init__(self, recipe_name: str, amount=1, extra_product_rate_dict=None):
        dp_tracker: DependencyTracker = DependencyTracker(recipe_name, amount, extra_product_rate_dict)

        self.total_recipe_req_dict = dp_tracker.initial_total_recipe_req_dict
        self.total_item_req_dict = self.counter_add_dict([dp_tracker.initial_total_item_req_dict, dp_tracker.cannot_process_item_dict], 'pr')['pr']

        self.oil_obj = OilProcessor(dp_tracker.cannot_process_item_dict, extra_product_rate_dict=extra_product_rate_dict)

        if dp_tracker.cannot_process_item_dict != {}:
            item_dict_list = [self.total_item_req_dict, self.oil_obj.oil_item_needed]
            recipe_dict_list = [self.total_recipe_req_dict, self.oil_obj.oil_recipe_needed]
            self.merged_recipe_dict = self.counter_add_dict(recipe_dict_list, 'recipe')
            self.merged_item_dict = self.counter_add_dict(item_dict_list, 'item')
        else:
            self.merged_recipe_dict = {'general_recipe': self.total_recipe_req_dict,
                                       'oil_recipe': {}}
            self.merged_item_dict = {'general_item': self.total_item_req_dict,
                                     'oil_item': {}}

    def counter_add_dict(self, dict_list: list, prefix: str = ''):
        counter_obj = Counter({})
        for i in range(len(dict_list)):
            counter_obj += Counter(dict_list[i])
        to_return_dict = {
            prefix: dict(counter_obj)
        }
        return to_return_dict
