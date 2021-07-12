from data.recipe_dict import recipe_dict


class FactorioOilRefinery:
    how_many_adv: float
    heavy_to_light_amount: float
    light_to_gas_amount: float

    def __init__(self, petroleum_gas=0, light_oil=0, heavy_oil=0):
        self.petroleum_gas_need = petroleum_gas
        self.light_oil_need = light_oil
        self.heavy_oil_need = heavy_oil
        pass

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

    def advanced_oil_processing_no_cracking(self):
        pass

    def find_cracking_ratio(self, how_many_adv):
        need = [self.heavy_oil_need, self.light_oil_need, self.petroleum_gas_need]

        pass
