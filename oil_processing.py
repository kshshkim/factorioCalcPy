from data.recipe_dict import recipe_dict


# TODO advanced-oil-processing 이외 다른 방법 추가
class FactorioOilReqToRecipe:
    how_many_adv: float
    heavy_to_light_amount: float
    light_to_gas_amount: float
    extra: list

    def __init__(self, oil_need_dict, resource_consumption_ratio_dict):
        if resource_consumption_ratio_dict is None:
            resource_consumption_ratio_dict = {}
        self.resource_consumption_ratio_dict = resource_consumption_ratio_dict
        if oil_need_dict.get('petroleum-gas') is None:
            oil_need_dict['petroleum-gas']=0
        self.petroleum_gas_need = oil_need_dict['petroleum-gas']
        if oil_need_dict.get('light-oil') is None:
            oil_need_dict['light-oil']=0
        self.light_oil_need = oil_need_dict['light-oil']
        if oil_need_dict.get('heavy_oil') is None:
            oil_need_dict['heavy_oil']=0
        self.heavy_oil_need = oil_need_dict['heavy_oil']

        self.hoc_resource_consumption_ratio = 1
        self.loc_resource_consumption_ratio = 1

        for key in self.resource_consumption_ratio_dict.keys():
            if key == 'heavy-oil-cracking':
                self.hoc_resource_consumption_ratio = self.resource_consumption_ratio_dict[key]
            elif key == 'light-oil-cracking':
                self.loc_resource_consumption_ratio = self.resource_consumption_ratio_dict[key]
            elif key == 'advanced-oil-processing':
                self.adv_resource_consumption_ratio = self.resource_consumption_ratio_dict[key]

        self.advanced_oil_processing_plus_cracking()
        self.get_item_needed()

    def advanced_oil_processing_plus_cracking(self):

        adv = [25, 45, 55]
        need = [self.heavy_oil_need, self.light_oil_need, self.petroleum_gas_need]
        extra = [0, 0, 0]

        h2l = 3/(4*self.hoc_resource_consumption_ratio)
        l2p = 2/(3*self.loc_resource_consumption_ratio)

        a = need[0] / adv[0]
        for i in range(3):
            extra[i - 1] = adv[i - 1] * a
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
            before_cracked[i - 1] = adv[i - 1] * how_many_adv
        heavy_to_light_amount = before_cracked[0] - need[0]
        light_to_gas_amount = heavy_to_light_amount * 0.75 + before_cracked[1] - need[1]

        self.how_many_adv = how_many_adv
        self.heavy_to_light_amount = heavy_to_light_amount/(40*h2l)
        self.light_to_gas_amount = light_to_gas_amount/(30*l2p)
        self.extra = extra

    def get_recipe_needed(self):
        new_dict = {
            'advanced-oil-processing': self.how_many_adv,
            'heavy-oil-cracking': self.heavy_to_light_amount,
            'light-oil-cracking': self.light_to_gas_amount,
            # 'extra': self.extra
        }
        return new_dict

    def get_item_needed(self):
        ref_dict = self.get_recipe_needed()
        new_dict2 = {}
        for key in ref_dict:
            if ref_dict[key]!=0:
                ingredients_dict = recipe_dict[key]['ingredients']
                if key not in self.resource_consumption_ratio_dict:
                    self.resource_consumption_ratio_dict[key] = 1
                for key2 in ingredients_dict:
                    if new_dict2.get(key2) is None:
                        new_dict2[key2] = 0
                    new_dict2[key2] = new_dict2[key2] + ingredients_dict[key2]*ref_dict[key]*self.resource_consumption_ratio_dict[key]
        return new_dict2
