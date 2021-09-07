from FactorioCalcBase.dependency_dict_common_function import construct_dependedncy_dict
from FactorioCalcBase.recipe_class import RecipeClass


class UraniumProcessor:
    def __init__(self, cannot_process_dict: dict, extra_product_rate_dict: dict, use_kovarex: bool = False):
        self.extra_product_rate_dict = extra_product_rate_dict
        self.u235_needed = cannot_process_dict.get('uranium-235')
        if self.u235_needed is None:
            self.u235_needed = 0
        self.u238_needed = cannot_process_dict.get('uranium-238')
        if self.u238_needed is None:
            self.u238_needed = 0
        self.use_kovarex = use_kovarex
        self.item_needed = {}
        self.recipe_needed = {}
        self.extra = {}
        self.cannot_process_dict = {}
        if (self.u238_needed != 0) or (self.u235_needed != 0):
            self.initialize()


    def initialize(self):
        if self.use_kovarex is True:
            self.kovarex_override()
        else:
            self.uranium_processing()

    def uranium_processing(self):
        extra_product_rate = self.extra_product_rate_dict.get('uranium-processing')
        if extra_product_rate is None:
            extra_product_rate = 1
        uranium_recipe_obj = RecipeClass('uranium-processing')
        u235_result_count = uranium_recipe_obj.results['uranium-235']  # 0.007
        u238_result_count = uranium_recipe_obj.results['uranium-238']  # 0.993

        u235_std = self.u235_needed / (u235_result_count * extra_product_rate)
        u238_std = self.u238_needed / (u238_result_count * extra_product_rate)

        if u235_std > u238_std:
            up_recipe_needed = u235_std
            extra = {'uranium-238': (u235_std - u238_std) * u238_result_count}
        else:
            up_recipe_needed = u238_std
            extra = {'uranium-235': (u238_std - u235_std) * u235_result_count}
        self.extra = extra

        dict_list = construct_dependedncy_dict('uranium-processing', up_recipe_needed, self.extra_product_rate_dict)

        self.recipe_needed = dict_list[0]
        self.item_needed = dict_list[1]
        self.cannot_process_dict = dict_list[2]

        # 일반 -> 우라늄 -> 오일

    def uranium_ore_mining(self):
        pass

    def kovarex_override(self):

        pass
