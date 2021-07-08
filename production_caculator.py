from converted_data.recipe_info import recipe_info as recipe
from factorioItemclass import FactorioItem
import pprint

# production-time=energy_required/생산배수
# FactorioItem 필요

class ProductionCalc:
    def __init__(self, target_item, production_rate=1): # production_rate는 production_facility에 따라 달라짐.
        self.target=target_item
        self.total_req=FactorioItem(self.target).gettotalrequirements()
        self.production_rate=production_rate
        self.production_time = self.getproductiontime()
    pass

    def getproductiontime(self): # target_item
        production_time=recipe[self.target]['energy_required']/self.production_rate
        return production_time

    def get_total_facility(self):
        toreturndict={}



asd=ProductionCalc('processing-unit')


pprint.pp(asd.total_req)