import copy

import dependencydictbuilder
import recipe

ddb = dependencydictbuilder.DependencyDictBuilder()
recipe1=recipe.recipe

class DependencyCalc:
    def getdict(self, item):
        dpdict = ddb.dependencyFinder(item)
        return dpdict
    def getingredientperone(self,itemname):
        copiedrecipe=copy.deepcopy(recipe1)
        itemdictkeylist=list(copiedrecipe[itemname].keys())
        pquant = list(copiedrecipe[itemname]['results'].values())[0]
        if len(copiedrecipe[itemname]['results'].keys())<2:
            for ingredient in copiedrecipe[itemname]['ingredients']:
                copiedrecipe[itemname]['ingredients'][ingredient]=copiedrecipe[itemname]['ingredients'][ingredient]/pquant
            return copiedrecipe[itemname]['ingredients']
        else:
            pass
            # TODO 한 레시피에서 결과물이 여러개 나오는 경우는 나중에 할것

        #print(dpdictkeylist)

dc=DependencyCalc()
print(dc.getingredientperone('advanced-oil-processing'))
#print(recipe1['speed-module-3'].keys())