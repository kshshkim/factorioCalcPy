from data.recipe_dict import recipe_dict


# TODO 생산모듈에 따라서 비율이 가변적일 수 있음 씨발
class FactorioOilNeedToRecipe:
    how_many_adv: float
    heavy_to_light_amount: float
    light_to_gas_amount: float
    extra: list

    def __init__(self, oil_need_dict):
        if oil_need_dict.get('petroleum-gas') is None:
            oil_need_dict['petroleum-gas']=0
        self.petroleum_gas_need = oil_need_dict['petroleum-gas']
        if oil_need_dict.get('light-oil') is None:
            oil_need_dict['light-oil']=0
        self.light_oil_need = oil_need_dict['light-oil']
        if oil_need_dict.get('heavy_oil') is None:
            oil_need_dict['heavy_oil']=0
        self.heavy_oil_need = oil_need_dict['heavy_oil']
        self.advanced_oil_processing_plus_cracking()

    def advanced_oil_processing_plus_cracking(self):

        adv = [25, 45, 55]
        need = [self.heavy_oil_need, self.light_oil_need, self.petroleum_gas_need]
        extra = [0, 0, 0]

        a = need[0] / adv[0]
        for i in range(3):
            extra[i - 1] = adv[i - 1] * a
        extra[0] = 0

        if extra[1] < need[1]:
            b = (need[1] - extra[1]) / (adv[0] * 0.75 + adv[1])
            extra[2] = extra[2] + b * adv[2]
        else:
            b = 0
            extra[1] = extra[1] - need[1]

        extra[2] = extra[2] + (extra[1] * 2 / 3)

        if extra[2] < need[2]:
            c = (need[2] - extra[2]) / ((adv[0] * 0.5) + (adv[1] * 2 / 3) + adv[2])
        else:
            c = 0
            extra[2] = extra[2] - need[2]

        how_many_adv = a + b + c

        before_cracked = [0, 0, 0]
        for i in range(3):
            before_cracked[i - 1] = adv[i - 1] * how_many_adv
        heavy_to_light_amount = before_cracked[0] - self.heavy_oil_need
        light_to_gas_amount = heavy_to_light_amount * 0.75 + before_cracked[1] - need[1]

        self.how_many_adv = how_many_adv
        self.heavy_to_light_amount = heavy_to_light_amount
        self.light_to_gas_amount = light_to_gas_amount
        self.extra = extra

    def get_recipe_needed(self):
        new_dict = {
            'advanced-oil-processing': self.how_many_adv,
            'heavy-oil-cracking': self.heavy_to_light_amount,
            'light-oil-cracking': self.light_to_gas_amount,
            # 'extra': self.extra
        }
        print(new_dict)
        return new_dict
