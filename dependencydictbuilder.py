import recipe
import copy

recipe1 = recipe.recipe


class DependencyDictBuilder:
    def dependencyFinder_dict(self, item):
        newdict = self.getDictInfo_dict(item)

        if recipe1[item]['ingredients'] == '':
            print('no dependency for ' + str(item))
        else:
            print('there is dependency for ' + str(item))
            print('start chasing')
            newdict = self.addChildLayer(newdict)
        return newdict

    def getDictInfo_dict(self, item):
        return recipe1[item]

    def addChildLayer(self, ddict):
        ddict['child layer'] = {}
        for ingredient in list(ddict['ingredients'].keys()):
            ddict['child layer'][ingredient] = self.getDictInfo_dict(ingredient)
            if recipe1[ingredient]['ingredients'] != '':
                ddict['child layer'][ingredient] = self.addChildLayer(ddict['child layer'][ingredient])
        return ddict

    def getingredientperone_dict(self,itemname):
        copiedrecipe=copy.deepcopy(recipe1)
        pquant = self.getResultCount_float(itemname)
        if len(copiedrecipe[itemname]['results'].keys())<2:
            for ingredient in copiedrecipe[itemname]['ingredients']:
                copiedrecipe[itemname]['ingredients'][ingredient]=copiedrecipe[itemname]['ingredients'][ingredient]/pquant
            return copiedrecipe[itemname]['ingredients']
        else:
            pass

    def getResultCount_float(self, itemname):
        copiedrecipe = copy.deepcopy(recipe1)
        if recipe1[itemname]['results']=='':
            return int(1)
        elif len(list(copiedrecipe[itemname]['results'].keys()))<2:
            pquant=copiedrecipe[itemname]['results'][itemname]
            return pquant
        else:
            pass # TODO 다중출력레시피 손봐야함

    def totalReq_dict(self):

        pass

ddb=DependencyDictBuilder()
