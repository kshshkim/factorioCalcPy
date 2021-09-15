from FactorioCalcBase.recipe_class import RecipeClass
from FactorioCalcBase.oil_processing import OilProcessor
from FactorioCalcBase.uranium_processing import UraniumProcessor
from FactorioCalcBase.dependency_dict_common_function import counter_add_dict, merge_item_dicts, \
    construct_dependency_dict


class ProcessGeneral:
    def __init__(self, recipe_name: str, amount=1.0, extra_product_rate_dict=None):
        self.name = recipe_name
        self.amount = amount
        if extra_product_rate_dict is None:
            extra_product_rate_dict = {}
        self.extra_product_rate_dict = extra_product_rate_dict
        self.cannot_process_item_dict = {}
        self.item_req_dict = {}
        self.recipe_req_dict = {}
        self.construct_dicts()

    def construct_dicts(self):
        dict_list = construct_dependency_dict(self.name, self.amount, self.extra_product_rate_dict)

        self.recipe_req_dict = dict_list[0]
        self.item_req_dict = dict_list[1]
        self.cannot_process_item_dict = dict_list[2]


class ProcessExcepts:
    def __init__(self, cannot_process_dict: dict, extra_product_rate_dict: dict, use_kovarex=False):
        # general -> uranium -> oil

        uranium_obj = UraniumProcessor(cannot_process_dict=cannot_process_dict,
                                       extra_product_rate_dict=extra_product_rate_dict,
                                       use_kovarex=use_kovarex)
        uranium_cannot_process_dict = uranium_obj.cannot_process_dict
        merged_cannot_process_dict = counter_add_dict([cannot_process_dict, uranium_cannot_process_dict])

        oil_obj = OilProcessor(merged_cannot_process_dict[''], extra_product_rate_dict)

        item_dict_list = [uranium_obj.item_needed, oil_obj.item_needed]
        recipe_dict_list = [uranium_obj.recipe_needed, oil_obj.recipe_needed]

        self.item_req_dict = merge_item_dicts(item_dict_list)
        self.recipe_req_dict = counter_add_dict(recipe_dict_list)['']


class FullDependency:
    # TODO 하드코딩 정리
    def __init__(self, recipe_name: str, amount: float, extra_product_rate_dict: dict, use_kovarex=False):
        process_general: ProcessGeneral = ProcessGeneral(recipe_name, amount, extra_product_rate_dict)
        process_excepts: ProcessExcepts = ProcessExcepts(cannot_process_dict=process_general.cannot_process_item_dict,
                                                         extra_product_rate_dict=extra_product_rate_dict,
                                                         use_kovarex=use_kovarex)

        if process_general.cannot_process_item_dict != {}:
            item_dict_list = [process_general.item_req_dict, process_excepts.item_req_dict]
            recipe_dict_list = [process_general.recipe_req_dict, process_excepts.recipe_req_dict]
            self.merged_recipe_dict = counter_add_dict(recipe_dict_list, 'recipe')
            self.merged_item_dict = merge_item_dicts(item_dict_list)

        else:
            self.merged_recipe_dict = {'recipe': process_general.recipe_req_dict}
            self.merged_item_dict = process_general.recipe_req_dict
