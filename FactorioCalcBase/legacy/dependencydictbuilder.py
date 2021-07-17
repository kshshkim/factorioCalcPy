from FactorioCalcBase.legacy.data import recipe_dict

recipe1 = recipe_dict.recipe


class DependencyDictBuilder:
    def dependencyFinder_dict(self, item):
        newdict = self.getDictInfo_dict(item)

        if recipe1[item]['ingredients'] == '':
            print('no dependency for ' + str(item))
        else:
            print('there is dependency for ' + str(item))
            print('start chasing')
            newdict = self.add_child_layer(newdict)
        return newdict

    @staticmethod
    def getDictInfo_dict(item):
        return recipe1[item]

    def add_child_layer(self, ddict):
        ddict['child layer'] = {}
        for ingredient in list(ddict['ingredients'].keys()):  # 깊이우선
            ddict['child layer'][ingredient] = self.getDictInfo_dict(ingredient)
            if recipe1[ingredient]['ingredients'] != '':
                ddict['child layer'][ingredient] = self.add_child_layer(ddict['child layer'][ingredient])
        return ddict
