from FactorioCalcBase.recipe_class import RecipeClass
from FactorioCalcBase.data.binary import recipe_dict

# TODO advanced-oil-processing 이외 다른 방법 추가


class OilProcessor:
    def __init__(self, oil_need_dict, extra_product_rate_dict=None):
        self.how_many_adv = 0
        self.heavy_to_light_amount = 0
        self.light_to_gas_amount = 0
        self.extra = 0
        self.item_needed = {}
        self.oil_recipe_needed = {}
        self.non_oil_recipe_needed = {}
        self.oil_item_needed = {}
        if extra_product_rate_dict is None:
            extra_product_rate_dict = {}
        self.extra_product_rate_dict = extra_product_rate_dict
        if oil_need_dict.get('petroleum-gas') is None:
            oil_need_dict['petroleum-gas'] = 0
        self.petroleum_gas_need = oil_need_dict['petroleum-gas']
        if oil_need_dict.get('light-oil') is None:
            oil_need_dict['light-oil'] = 0
        self.light_oil_need = oil_need_dict['light-oil']
        if oil_need_dict.get('heavy_oil') is None:
            oil_need_dict['heavy_oil'] = 0
        self.heavy_oil_need = oil_need_dict['heavy_oil']

        self.hoc_extra_product_ratio = 1
        self.loc_extra_product_ratio = 1

        for key in self.extra_product_rate_dict.keys():
            if key == 'heavy-oil-cracking':
                self.hoc_extra_product_ratio = self.extra_product_rate_dict[key]
            elif key == 'light-oil-cracking':
                self.loc_extra_product_ratio = self.extra_product_rate_dict[key]
            elif key == 'advanced-oil-processing':
                self.adv_resource_consumption_ratio = self.extra_product_rate_dict[key]

        self.advanced_oil_processing_plus_cracking()
        self.update_oil_recipe_needed()
        # self.update_oil_item_needed()
        # self.update_non_oil_recipe_needed()

    def advanced_oil_processing_plus_cracking(self):
        adv = [25, 45, 55]  # advanced_oil_processing 생산량, 중유, 경유, 가스 순서
        if 'advanced-oil-processing' in self.extra_product_rate_dict.keys():
            for i in range(len(adv)):
                adv[i] = adv[i]*self.extra_product_rate_dict['advanced-oil-processing']

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

    def update_oil_recipe_needed(self):
        # 먼저 advanced_oil_processing_plus_cracking 이 실행되어야함.
        new_dict = {
            'advanced-oil-processing': self.how_many_adv,
            'heavy-oil-cracking': self.heavy_to_light_amount,
            'light-oil-cracking': self.light_to_gas_amount,
            # 'extra': self.extra
        }
        self.oil_recipe_needed = new_dict
        self.update_oil_item_needed()
        for recipe in ['water', 'crude-oil']:
            new_rcp_obj = RecipeClass(recipe)
            if self.oil_recipe_needed.get(recipe) is None:
                self.oil_recipe_needed[recipe] = 0
            self.oil_recipe_needed[recipe] += self.oil_item_needed[recipe]/new_rcp_obj.get_results_count()

    def update_oil_item_needed(self):
        new_dict = {}
        for key in self.oil_recipe_needed.keys():
            for each_ingredient in recipe_dict[key]['ingredients'].keys():
                if new_dict.get(each_ingredient) is None:
                    new_dict[each_ingredient] = 0
                new_dict[each_ingredient] += recipe_dict[key]['ingredients'][each_ingredient]*self.oil_recipe_needed[key]
        self.oil_item_needed = new_dict

