from FactorioCalcBase.recipe_class import RecipeClass
from FactorioCalcBase.oil_processing import OilProcessor
from FactorioCalcBase.common_function import add_to_item_dict, dict_add_number, counter_add_dict, merge_item_dicts
from collections import deque


class DependencyTracker:
    def __init__(self, recipe_name: str, amount=1, extra_product_rate_dict=None):
        self.name = recipe_name
        self.amount = amount
        self.recipe_obj = RecipeClass(recipe_name, amount=amount)
        if extra_product_rate_dict is None:
            extra_product_rate_dict = {}
        self.extra_product_rate_dict = extra_product_rate_dict
        self.cannot_process_item_dict = {}
        self.item_needed_dict = self.recipe_obj.ingredients
        self.results = self.recipe_obj.results
        self.initial_total_item_req_dict = {}
        self.initial_total_recipe_req_dict = {}
        self.construct_dicts()

    def construct_dicts(self):
        obj_search_queue = deque([self.recipe_obj])
        item_needed_queue = deque([])
        cannot_process_item_dict = {}
        total_recipe_needed_dict = {self.recipe_obj.name: self.recipe_obj.amount}
        total_item_needed_dict = {}

        while obj_search_queue:
            current = obj_search_queue[0]
            if current.ingredients != '':
                for key, val in current.ingredients.items():
                    to_append = [key, val * current.amount]
                    item_needed_queue.append(to_append)
                    add_to_item_dict(total_item_needed_dict, item_name=key, item_amount=val*current.amount, required_by=current.name)

            while item_needed_queue:  # [0] = current, [][0] = name [][1] = amount
                if self.find_recipe(item_needed_queue[0]) != -1:
                    returned = self.find_recipe(item_needed_queue[0])
                    # returned, [0]: name, [1]: amount
                    new_rcp_obj = RecipeClass(returned[0], amount=returned[1])
                    dict_add_number(total_recipe_needed_dict, key=returned[0], val=returned[1])
                    obj_search_queue.append(new_rcp_obj)
                else:
                    # item_needed_queue[0][b], 0: index, b:0: item name, b:1: item amount
                    item_name = item_needed_queue[0][0]
                    item_amount = item_needed_queue[0][1]
                    dict_add_number(cannot_process_item_dict, key=item_name, val=item_amount)
                item_needed_queue.popleft()
            obj_search_queue.popleft()

        self.initial_total_recipe_req_dict = total_recipe_needed_dict
        self.initial_total_item_req_dict = total_item_needed_dict
        self.cannot_process_item_dict = cannot_process_item_dict

    def find_recipe(self, needed_list):
        item_name = needed_list[0]
        item_amount = needed_list[1]

        recipe_name = ''
        trc = RecipeClass(item_name)
        # name_results_match 가 아니면 따로 처리

        if trc.is_name_results_match():
            recipe_name = item_name
        elif item_name in ['petroleum-gas', 'light-oil', 'heavy-oil', 'solid-fuel', 'raw-fish', 'wood', 'uranium-235', 'uranium-238']:  # TODO 우라늄 제작법
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
    def __init__(self, recipe_name: str, amount: float, extra_product_rate_dict: dict):
        dp_tracker: DependencyTracker = DependencyTracker(recipe_name, amount, extra_product_rate_dict)

        self.total_recipe_req_dict = dp_tracker.initial_total_recipe_req_dict
        self.total_item_req_dict = dp_tracker.initial_total_item_req_dict
        self.oil_obj = OilProcessor(dp_tracker.cannot_process_item_dict, extra_product_rate_dict=extra_product_rate_dict)

        if dp_tracker.cannot_process_item_dict != {}:
            item_dict_list = [self.total_item_req_dict, self.oil_obj.oil_item_needed]
            recipe_dict_list = [self.total_recipe_req_dict, self.oil_obj.oil_recipe_needed]
            self.merged_recipe_dict = counter_add_dict(recipe_dict_list, 'recipe')
            self.merged_item_dict = merge_item_dicts(item_dict_list)

        else:
            self.merged_recipe_dict = {'general_recipe': self.total_recipe_req_dict,
                                       'oil_recipe': {}}
            self.merged_item_dict = {'general_item': self.total_item_req_dict,
                                     'oil_item': {}}

