from recipe import recipe


class dictcalc:
    def getresultscount_float(self,itemname):
        if recipe[itemname]['results'][itemname] == 1 or recipe[itemname]['results'][itemname] == 1.0:
            resultcount=1.0

        return resultcount

    def getingredientsperone_dict(self,tocalcdict):
        mothersname=tocalcdict['name']
        if self.getresultscount_float(tocalcdict['name']) == 1:
            ingredientsperone = tocalcdict['ingredients']
        else:
            for ingredient in tocalcdict['ingredients'].keys():
                tocalcdict['ingredients'][ingredient]=tocalcdict['ingredients'][ingredient]/self.getresultscount_float(tocalcdict['name'])
            ingredientsperone = tocalcdict['ingredients']
        return ingredientsperone
