import recipe
import copy

recipe1 = recipe.recipe


class DependencyDictBuilder:
    def dependencyFinder(self, item):
        newdict = self.getDictInfo(item)

        if recipe1[item]['ingredients'] == '':
            print('no dependency for ' + str(item))
        else:
            print('there is dependency for ' + str(item))
            print('start chasing')
            newdict = self.addChildLayer(newdict)
        return newdict

    def getDictInfo(self, item):
        return recipe1[item]

    def addChildLayer(self, dict):
        dict['child layer'] = {}
        for ingredient in list(dict['ingredients'].keys()):
            dict['child layer'][ingredient] = self.getDictInfo(ingredient)
            if recipe1[ingredient]['ingredients'] != '':
                dict['child layer'][ingredient] = self.addChildLayer(dict['child layer'][ingredient])
        return dict

    def getingredientperone(self,itemname):
        copiedrecipe=copy.deepcopy(recipe1)
        pquant = self.getpquant(itemname)
        if len(copiedrecipe[itemname]['results'].keys())<2:
            for ingredient in copiedrecipe[itemname]['ingredients']:
                copiedrecipe[itemname]['ingredients'][ingredient]=copiedrecipe[itemname]['ingredients'][ingredient]/pquant
            return copiedrecipe[itemname]['ingredients']
        else:
            pass

    def getpquant(self,itemname):
        copiedrecipe = copy.deepcopy(recipe1)
        if recipe1[itemname]['results']=='':
            return int(1)
        elif len(list(copiedrecipe[itemname]['results'].keys()))<2:
            pquant=copiedrecipe[itemname]['results'][itemname]
            return pquant
        else:
            pass # TODO 다중출력레시피 손봐야함

    def totalReq(self,itemname):
        newdict = self.getDictInfo(itemname)


ddb=DependencyDictBuilder()
