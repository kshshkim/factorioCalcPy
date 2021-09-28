from FactorioCalcBase.recipe import Recipe
from FactorioCalcBase.dependency_dict_common_function import add_to_item_dict, dict_add_number
from collections import Counter

# TODO advanced-oil-processing 이외 다른 방법 추가


class OilProcessor:
    def __init__(self, process_excepts_dict: dict, extra_product_rate_dict=None):
        self.how_many_adv = 0
        self.heavy_to_light_amount = 0
        self.light_to_gas_amount = 0
        self.extra = 0
        self.item_needed = {}
        self.recipe_needed = {}
        self.item_needed = {}
        if extra_product_rate_dict is None:
            extra_product_rate_dict = {}
        self.extra_product_rate_dict = extra_product_rate_dict
        if process_excepts_dict.get('petroleum-gas') is None:
            process_excepts_dict['petroleum-gas'] = 0
        self.petroleum_gas_need = process_excepts_dict['petroleum-gas']
        if process_excepts_dict.get('light-oil') is None:
            process_excepts_dict['light-oil'] = 0
        self.light_oil_need = process_excepts_dict['light-oil']
        if process_excepts_dict.get('heavy_oil') is None:
            process_excepts_dict['heavy_oil'] = 0
        self.heavy_oil_need = process_excepts_dict['heavy_oil']

        self.hoc_extra_product_ratio = 1
        self.loc_extra_product_ratio = 1
        self.adv_resource_consumption_ratio = 1

        for key in self.extra_product_rate_dict.keys():
            if key == 'heavy-oil-cracking':
                self.hoc_extra_product_ratio = self.extra_product_rate_dict[key]
            elif key == 'light-oil-cracking':
                self.loc_extra_product_ratio = self.extra_product_rate_dict[key]
            elif key == 'advanced-oil-processing':
                self.adv_resource_consumption_ratio = self.extra_product_rate_dict[key]

        self.advanced_oil_processing_plus_cracking()
        self.update_recipe_item_needed()

    def advanced_oil_processing_plus_cracking(self):
        aop_obj = Recipe('advanced-oil-processing')
        adv = [aop_obj.results['heavy-oil'], aop_obj.results['heavy-oil'], aop_obj.results['petroleum-gas']]  # default [25, 45, 55] advanced_oil_processing 생산량, 중유, 경유, 가스 순서
        for i in range(3):
            adv[i] = adv[i]*self.adv_resource_consumption_ratio

        need = [self.heavy_oil_need, self.light_oil_need, self.petroleum_gas_need]
        extra = [0, 0, 0]

        h2l = (3 * self.hoc_extra_product_ratio) / 4
        l2p = (2 * self.loc_extra_product_ratio) / 3

        a = need[0] / adv[0]
        for i in range(3):
            extra[i] = adv[i] * a
        extra[0] = 0

        if extra[1] < need[1]:
            b = (need[1] - extra[1]) / (adv[0] * h2l + adv[1])
            extra[2] = extra[2] + b * adv[2]
        else:
            b = 0
            extra[1] = extra[1] - need[1]

        extra[2] = extra[2] + (extra[1] * l2p)

        if extra[2] < need[2]:
            c = (need[2] - extra[2]) / ((adv[0] * h2l * l2p) + (adv[1] * l2p) + adv[2])
        else:
            c = 0
            extra[2] = extra[2] - need[2]

        how_many_adv = a + b + c

        before_cracked = [0, 0, 0]
        for i in range(3):
            before_cracked[i] = adv[i] * how_many_adv
        extra_heavy_amount = before_cracked[0] - need[0]
        extra_light_amount = extra_heavy_amount * h2l + before_cracked[1] - need[1]

        self.how_many_adv = how_many_adv
        self.heavy_to_light_amount = extra_heavy_amount / (40 * h2l)
        self.light_to_gas_amount = extra_light_amount / (30 * l2p)
        self.extra = extra

    def update_recipe_item_needed(self):
        # 먼저 advanced_oil_processing_plus_cracking 이 실행되어야함.
        new_dict = {
            'advanced-oil-processing': self.how_many_adv,
            'heavy-oil-cracking': self.heavy_to_light_amount,
            'light-oil-cracking': self.light_to_gas_amount,
            # 'extra': self.extra
        }

        oil_recp_dict = {}
        oil_item_dict = {}

        for key, val in new_dict.items():
            for key2, val2 in Recipe(key).ingredients.items():
                if key2 not in ['heavy-oil', 'light-oil', 'petroleum-gas']:  # 경유 중유 가스는 이미 레시피 필요량 계산 완료됨.
                    new_recp = Recipe(key2)
                    how_many = val*val2/new_recp.get_results_count()  #  val2/new_recp.get_results_count() <= 생산물 1 단위당 레시피 필요량
                    dict_add_number(oil_recp_dict, new_recp.name, how_many)

                add_to_item_dict(oil_item_dict, key2, val*val2, key)

        self.recipe_needed = dict(Counter(new_dict) + Counter(oil_recp_dict))
        self.item_needed = oil_item_dict
