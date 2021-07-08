from recipe_info import recipe
import copy
from collections import Counter


class FactorioItem:
    def __init__(self, putname):
        self.name = putname
        self.energy_required = recipe[self.name]['energy_required']
        self.ingredients = recipe[self.name]['ingredients']
        self.results = recipe[self.name]['results']
        self.icon = recipe[self.name]['icon']
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

    def makechild(self, ancestors_needs=1.0): # TODO totalreqdict 메소드 분리하기
        self.children = {}
        self.ingredientsperone = self.getingredientsperone()
        amount_ancestors_needs = copy.deepcopy(ancestors_needs)
        self.totalreqdict = {}
        if self.ingredients != '':
            for key in self.ingredients.keys():
                child = FactorioItem(key)
                child.mother = self
                child.amount_mother_needs = float(self.ingredientsperone[key])
                child.amount_ancestors_needs = child.amount_mother_needs * amount_ancestors_needs
                self.children[child.name + ' *' + str(child.amount_ancestors_needs)] = child  # self.children.values() <- children 목록,
                # children 변수에 지정된 딕셔너리에 FactorioItem 타입 오브젝트를 value로 저장, list로 하는게 나을지 이게 나을지 아직 못 정함
                child.makechild(child.amount_ancestors_needs)
                self.totalreqdict[child.name] = child.amount_ancestors_needs

                selfdict = Counter(self.totalreqdict)
                childdict = Counter(child.totalreqdict)

                self.totalreqdict = selfdict + childdict
                self.totalreqdict = dict(self.totalreqdict)

    def gettotalrequirements(self):
        self.makechild()
        return self.totalreqdict
