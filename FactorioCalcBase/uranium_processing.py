from FactorioCalcBase.dependency_dict_common_function import construct_dependency_dict, add_to_item_dict
from FactorioCalcBase.recipe import Recipe


class UraniumProcessor:
    def __init__(self, process_excepts_dict: dict, extra_product_rate_dict: dict, use_kovarex: bool = False):
        self.extra_product_rate_dict = extra_product_rate_dict
        self.u235_needed = process_excepts_dict.get('uranium-235')
        if self.u235_needed is None:
            self.u235_needed = 0
        self.u238_needed = process_excepts_dict.get('uranium-238')
        if self.u238_needed is None:
            self.u238_needed = 0
        self.use_kovarex = use_kovarex
        self.item_needed = {}
        self.recipe_needed = {}
        self.extra = {}
        self.process_excepts_dict = {}

        self.total_u238_needed_by_kov = 0
        self.total_kov_recipe_needed_amount = 0
        self.total_up_recipe_needed_amount = 0
        self.up_u238_result_count = 0
        self.up_u235_result_count = 0
        self.kov_result_count = 0
        self.up_extra_product_rate = extra_product_rate_dict.get('uranium_processing')
        if self.up_extra_product_rate is None:
            self.up_extra_product_rate = 1
        self.kov_extra_product_rate = extra_product_rate_dict.get('kovarex-enrichment-process')
        if self.kov_extra_product_rate is None:
            self.kov_extra_product_rate = 1
        self.up_u235_std_needed = 0
        self.up_u238_std_needed = 0

        if (self.u238_needed != 0) or (self.u235_needed != 0):
            self.initialize()

    def initialize(self):
        self.var_set()

        if self.use_kovarex is True:
            self.kovarex_override()
        else:
            self.uranium_processing()

    def var_set(self):

        up_recipe_obj = Recipe('uranium-processing')

        self.up_u235_result_count = up_recipe_obj.results['uranium-235']
        self.up_u238_result_count = up_recipe_obj.results['uranium-238']
        self.up_u235_std_needed = self.u235_needed / (self.up_u235_result_count * self.up_extra_product_rate)
        self.up_u238_std_needed = self.u238_needed / (self.up_u238_result_count * self.up_extra_product_rate)

        kov_obj = Recipe("kovarex-enrichment-process")
        self.kov_result_count = kov_obj.results.get('uranium-235')

    def uranium_processing(self):
        u235_std = self.up_u235_std_needed
        u238_std = self.up_u238_std_needed

        if u235_std > u238_std:
            up_recipe_needed = u235_std
            extra = {'uranium-238': (u235_std - u238_std) * self.up_u238_result_count}
        else:
            up_recipe_needed = u238_std
            extra = {'uranium-235': (u238_std - u235_std) * self.up_u235_result_count}
        self.extra = extra
        self.total_up_recipe_needed_amount = up_recipe_needed
        dict_list = construct_dependency_dict('uranium-processing', up_recipe_needed, self.extra_product_rate_dict)

        self.recipe_needed = dict_list[0]
        self.item_needed = dict_list[1]
        self.process_excepts_dict = dict_list[2]

    # kovarex 1개 --
    # 필요(u238 3개)
    # 산출{
    #     kov-u235: kov_rc + kov_epr,
    #     up-u235: (up u235 생산량)*(up 레시피 필요량)
    #              (0.007*up_epr)*(3/(0.993)/up_epr)
    #              (up_u235_count*up_epr)*(kov_u238_needed/up_u238_count)/up_epr
    #     }
    # kov 1개당 산출 = u235+up-u235

    def kovarex_override(self):

        if self.up_u238_std_needed <= self.up_u235_std_needed:
            kov_obj = Recipe("kovarex-enrichment-process")
            kov_rc = self.kov_result_count
            kov_epr = self.kov_extra_product_rate

            up_epr = self.up_extra_product_rate
            up_u235_rc = self.up_u235_result_count
            up_u238_rc = self.up_u238_result_count
            kov_u238_needed = kov_obj.ingredients.get('uranium-238')

            up_rcp_needed_per_one_kov = (kov_u238_needed/up_u238_rc)/up_epr

            kov_u235_output = kov_rc * kov_epr
            up_u235_output = (up_u235_rc * up_epr)*up_rcp_needed_per_one_kov
            u235_output_per_one_kov = kov_u235_output + up_u235_output
            u235_produced_by_up = self.up_u238_std_needed * self.up_u235_result_count

            self.total_kov_recipe_needed_amount = (self.u235_needed - u235_produced_by_up) / u235_output_per_one_kov
            self.total_up_recipe_needed_amount = self.up_u238_std_needed + (self.total_kov_recipe_needed_amount * up_rcp_needed_per_one_kov)
            self.total_u238_needed_by_kov = self.total_kov_recipe_needed_amount * kov_u238_needed

            self.construct_total_dict()

    def construct_total_dict(self):

        dict_list = construct_dependency_dict('uranium-processing', self.total_up_recipe_needed_amount, self.extra_product_rate_dict)

        self.recipe_needed = dict_list[0]
        self.item_needed = dict_list[1]
        self.process_excepts_dict = dict_list[2]

        if self.use_kovarex is True:
            self.recipe_needed['kovarex-enrichment-process'] = self.total_kov_recipe_needed_amount
            add_to_item_dict(self.item_needed, 'uranium-238', self.total_u238_needed_by_kov, 'kovarex-enrichment-process')
