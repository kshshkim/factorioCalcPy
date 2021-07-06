from recipe import recipe
import copy


class factorioItem:
    def __init__(self, putname):
        self.name = putname
        self.energy_required = recipe[self.name]['energy_required']
        self.ingredients = recipe[self.name]['ingredients']
        self.results = recipe[self.name]['results']
        # self.ingredientsperone=self.getingredientsperone()

    def getingredientsperone(self):
        ingredientsdict = copy.deepcopy(self.ingredients)
        if self.ingredients != '':
            if len(list(self.results.keys())) == 1:
                if self.results[self.name] == 1 or self.results[self.name] == 1.0:
                    return ingredientsdict
                else:
                    for ingredient in ingredientsdict.keys():
                        ingredientsdict[ingredient] = ingredientsdict[ingredient] / self.results[self.name]
                    return ingredientsdict
        else:
            pass  # TODO 결과물이 여럿인 레시피는 나중에

    def makechild(self, ancestors_needs=1.0):
        self.children = {}
        self.ingredientsperone = self.getingredientsperone()
        amount_ancestors_needs = copy.deepcopy(ancestors_needs)
        if self.ingredients != '':
            for key in self.ingredients.keys():
                child = factorioItem(key)
                child.mother = self
                child.amount_mother_needs = self.ingredientsperone[key]
                child.amount_ancestors_needs = child.amount_mother_needs * amount_ancestors_needs
                self.children[
                    child.name] = child  # children 변수에 지정된 딕셔너리에 factorioItem 타입 오브젝트를 value로 저장, list로 하는게 나을지 이게 나을지 아직 못 정함
                child.makechild(child.amount_ancestors_needs)


gchip = factorioItem('processing-unit')
gchip.makechild()

# ggchip = factorio
print(gchip.getingredientsperone())
