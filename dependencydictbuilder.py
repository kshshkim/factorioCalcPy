import recipe

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
