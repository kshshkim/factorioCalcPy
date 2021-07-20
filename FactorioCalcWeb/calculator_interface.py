from FactorioCalcBase.calculator_base import FactorioCalculatorBase


class CalcInstance:
    def __init__(self):
        self.base_obj = FactorioCalculatorBase()
        self.config = {
            'recipe_name': 'advanced-circuit',
            'recipe_amount': '1',
            'mining_research_modifier': None,
        }

    def change_config(self, key: str, value):
        if self.config.get(key) is not None:
            self.config[key] = value

