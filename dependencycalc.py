import copy

import dependencydictbuilder
import recipe

ddb = dependencydictbuilder.DependencyDictBuilder()
recipe1=recipe.recipe

class DependencyCalc:
    def getdict(self, item):
        dpdict = ddb.dependencyFinder(item)
        return dpdict
            # TODO 한 레시피에서 결과물이 여러개 나오는 경우는 나중에 할것

        #print(dpdictkeylist)

dc=DependencyCalc()
print(dc.getingredientperone('iron-plate'))
#print(recipe1['speed-module-3'].keys())