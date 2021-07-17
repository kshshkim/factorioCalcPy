from FactorioCalcBase.legacy.factorio_item_class import FactorioItem
import copy


def make_child(self, ancestors_needs=1.0, extra_product_dict={}):
    self.children = {}
    self.ingredients_per_one = self.get_ingredients_per_one()
    amount_ancestors_needs = copy.deepcopy(ancestors_needs)
    if self.ingredients != '':
        for key in self.ingredients.keys():
            child = FactorioItem(key)
            child.mother = self
            child.amount_mother_needs = float(self.ingredients_per_one[key])
            child.amount_ancestors_needs = child.amount_mother_needs * amount_ancestors_needs
            self.children[child.name + ' *' + str(
                child.amount_ancestors_needs)] = child  # self.children.values() <- children 목록,
            # children 변수에 지정된 딕셔너리에 FactorioItem 타입 오브젝트를 value로 저장, list로 하는게 나을지 이게 나을지 아직 못 정함
            child.make_child(child.amount_ancestors_needs)
