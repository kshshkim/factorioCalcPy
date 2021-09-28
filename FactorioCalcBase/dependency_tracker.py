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
        self.process_excepts_dict = {}
        self.item_req_dict = {}
        self.recipe_req_dict = {}
        self.construct_dicts()

    def construct_dicts(self):
        dict_list = construct_dependency_dict(self.name, self.amount, self.extra_product_rate_dict)

        self.recipe_req_dict = dict_list[0]
        self.item_req_dict = dict_list[1]
        self.process_excepts_dict = dict_list[2]


class ProcessExcepts:
    def __init__(self, process_excepts_dict: dict, extra_product_rate_dict: dict, use_kovarex=False):
        # general -> uranium -> oil

        uranium_obj = UraniumProcessor(process_excepts_dict=process_excepts_dict,
                                       extra_product_rate_dict=extra_product_rate_dict,
                                       use_kovarex=use_kovarex)
        remain_excepts_after_up = uranium_obj.process_excepts_dict
        merged_excepts_dict = counter_add_dict([process_excepts_dict, remain_excepts_after_up])

        oil_obj = OilProcessor(merged_excepts_dict[''], extra_product_rate_dict)

        item_dict_list = [uranium_obj.item_needed, oil_obj.item_needed]
        recipe_dict_list = [uranium_obj.recipe_needed, oil_obj.recipe_needed]

        self.item_req_dict = merge_item_dicts(item_dict_list)
        self.recipe_req_dict = counter_add_dict(recipe_dict_list)['']


class FullDependency:
    def __init__(self, recipe_name: str, amount: float, extra_product_rate_dict: dict, use_kovarex=False):
        process_general: ProcessGeneral = ProcessGeneral(recipe_name, amount, extra_product_rate_dict)
        process_excepts: ProcessExcepts = ProcessExcepts(process_excepts_dict=process_general.process_excepts_dict,
                                                         extra_product_rate_dict=extra_product_rate_dict,
                                                         use_kovarex=use_kovarex)

        item_dict_list = [process_general.item_req_dict, process_excepts.item_req_dict]
        recipe_dict_list = [process_general.recipe_req_dict, process_excepts.recipe_req_dict]
        self.merged_recipe_dict = counter_add_dict(recipe_dict_list, 'recipe')
        self.merged_item_dict = merge_item_dicts(item_dict_list)
