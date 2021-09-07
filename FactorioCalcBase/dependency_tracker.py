from FactorioCalcBase.recipe_class import RecipeClass
from FactorioCalcBase.oil_processing import OilProcessor
from FactorioCalcBase.uranium_processing import UraniumProcessor
from FactorioCalcBase.dependency_dict_common_function import add_to_item_dict, dict_add_number, counter_add_dict, merge_item_dicts, construct_dependedncy_dict
from collections import deque




# def construct_dependedncy_dict(recipe_name: str, recipe_amount: float, extra_product_rate_dict: dict):
#     recipe_obj = RecipeClass(recipe_name, recipe_amount)
#
#     obj_search_queue = deque([recipe_obj])
#     item_needed_queue = deque([])
#     cannot_process_item_dict = {}
#     total_recipe_needed_dict = {recipe_obj.name: recipe_obj.amount}
#     total_item_needed_dict = {}
#
#     while obj_search_queue:
#         current = obj_search_queue[0]
#         if current.ingredients != '':
#             for key, val in current.ingredients.items():
#                 to_append = [key, val * current.amount]
#                 item_needed_queue.append(to_append)
#                 add_to_item_dict(total_item_needed_dict, item_name=key, item_amount=val * current.amount,
#                                  required_by=current.name)
#
#         while item_needed_queue:  # [0] = current, [][0] = name [][1] = amount
#             found_recipe = find_recipe(item_needed_queue[0], extra_product_rate_dict)
#
#             if found_recipe == -1:
#                 # item_needed_queue[0][b], 0: index, b:0: item name, b:1: item amount
#                 item_name = item_needed_queue[0][0]
#                 item_amount = item_needed_queue[0][1]
#                 dict_add_number(cannot_process_item_dict, key=item_name, val=item_amount)
#             else:
#                 returned = find_recipe(item_needed_queue[0], extra_product_rate_dict)
#                 # returned, [0]: name, [1]: amount
#                 new_rcp_obj = RecipeClass(returned[0], amount=returned[1])
#                 dict_add_number(total_recipe_needed_dict, key=returned[0], val=returned[1])
#                 obj_search_queue.append(new_rcp_obj)
#             item_needed_queue.popleft()
#         obj_search_queue.popleft()
#
#     return [total_recipe_needed_dict, total_item_needed_dict, cannot_process_item_dict]


class DependencyTracker:
    def __init__(self, recipe_name: str, amount=1.0, extra_product_rate_dict=None):
        self.name = recipe_name
        self.amount = amount
        self.recipe_obj = RecipeClass(recipe_name, amount=amount)
        if extra_product_rate_dict is None:
            extra_product_rate_dict = {}
        self.extra_product_rate_dict = extra_product_rate_dict
        self.cannot_process_item_dict = {}
        self.item_needed_dict = self.recipe_obj.ingredients
        self.results = self.recipe_obj.results
        self.item_req_dict = {}
        self.recipe_req_dict = {}
        self.construct_dicts()

    def construct_dicts(self):
        dict_list = construct_dependedncy_dict(self.name, self.amount, self.extra_product_rate_dict)

        self.recipe_req_dict = dict_list[0]
        self.item_req_dict = dict_list[1]
        self.cannot_process_item_dict = dict_list[2]


class ProcessExcepts:
    def __init__(self, cannot_process_dict: dict, extra_product_rate_dict: dict):
        # general -> uranium -> oil

        uranium_obj = UraniumProcessor(cannot_process_dict=cannot_process_dict, extra_product_rate_dict=extra_product_rate_dict)
        uranium_cannot_process_dict = uranium_obj.cannot_process_dict
        merged_cannot_process_dict = counter_add_dict([cannot_process_dict, uranium_cannot_process_dict])

        oil_obj = OilProcessor(merged_cannot_process_dict[''], extra_product_rate_dict)

        item_dict_list = [uranium_obj.item_needed, oil_obj.item_needed]
        recipe_dict_list = [uranium_obj.recipe_needed, oil_obj.recipe_needed]

        self.item_req_dict = merge_item_dicts(item_dict_list)
        self.recipe_req_dict = counter_add_dict(recipe_dict_list)['']


class FullDependency:
    # TODO 하드코딩 정리
    def __init__(self, recipe_name: str, amount: float, extra_product_rate_dict: dict):
        process_general: DependencyTracker = DependencyTracker(recipe_name, amount, extra_product_rate_dict)
        process_excepts: ProcessExcepts = ProcessExcepts(cannot_process_dict=process_general.cannot_process_item_dict, extra_product_rate_dict=extra_product_rate_dict)

        if process_general.cannot_process_item_dict != {}:
            item_dict_list = [process_general.item_req_dict, process_excepts.item_req_dict]
            recipe_dict_list = [process_general.recipe_req_dict, process_excepts.recipe_req_dict]
            self.merged_recipe_dict = counter_add_dict(recipe_dict_list, 'recipe')
            self.merged_item_dict = merge_item_dicts(item_dict_list)

        else:
            self.merged_recipe_dict = {'recipe': process_general.recipe_req_dict}
            self.merged_item_dict = process_general.recipe_req_dict

