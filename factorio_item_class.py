from data.recipe_dict import recipe_dict
import copy


class FactorioItem:
    def __init__(self, putname):
        self.name = putname
        self.energy_required = recipe_dict[self.name]['energy_required']
        self.ingredients = recipe_dict[self.name]['ingredients']
        self.results = recipe_dict[self.name]['results']
        self.subgroup = recipe_dict[self.name]['subgroup']
        self.icon = recipe_dict[self.name]['icon']
        self.amount_ancestors_needs = 1
        # self.ingredients_per_one=self.getingredientsperone()

    def get_ingredients_per_one(self):
        ingredients_dict = copy.deepcopy(self.ingredients)
        if self.ingredients != '':
            if len(list(self.results.keys())) == 1:
                if self.results[self.name] == 1 or self.results[self.name] == 1.0:
                    return ingredients_dict
                else:
                    for ingredient in ingredients_dict.keys():
                        ingredients_dict[ingredient] = ingredients_dict[ingredient] / self.results[self.name]
                    return ingredients_dict
        else:
            pass  # TODO 결과물이 여럿인 레시피는 나중에

    # def make_child(self, ancestors_needs=1.0, extra_product_dict={}):
    #     self.children = {}
    #     self.ingredients_per_one = self.get_ingredients_per_one()
    #     amount_ancestors_needs = copy.deepcopy(ancestors_needs)
    #     if self.ingredients != '':
    #         for key in self.ingredients.keys():
    #             child = FactorioItem(key)
    #             child.mother = self
    #             child.amount_mother_needs = float(self.ingredients_per_one[key])
    #             child.amount_ancestors_needs = child.amount_mother_needs * amount_ancestors_needs
    #             self.children[child.name + ' *' + str(
    #                 child.amount_ancestors_needs)] = child  # self.children.values() <- children 목록,
    #             # children 변수에 지정된 딕셔너리에 FactorioItem 타입 오브젝트를 value로 저장, list로 하는게 나을지 이게 나을지 아직 못 정함
    #             child.make_child(child.amount_ancestors_needs)

    def make_child(self, ancestors_needs=1.0, extra_product_dict={}): # TODO extra_product_dict를 반영해서 재료 요구량 조정
        self.amount_ancestors_needs=ancestors_needs
        self.total_req_dict={}
        search_queue=[self]
        while search_queue!=[]:
            current = search_queue[0]
            current.children = {}
            if current.ingredients != '':
                for key in current.ingredients.keys():
                    child=FactorioItem(key) # child obj 생성
                    child.mother=current
                    child.amount_mother_needs= float(current.get_ingredients_per_one()[key])
                    child.amount_ancestors_needs = child.amount_mother_needs * current.amount_ancestors_needs
                    current.children[child.name]=child
                    search_queue.append(child)
            if self.total_req_dict.get(current.name) == None:  # total_req_dict에 self.name과 일치하는 key가 없으면 추가
                self.total_req_dict[current.name] = 0
            self.total_req_dict[current.name] = self.total_req_dict[current.name] + current.amount_ancestors_needs

            search_queue.pop(0)

    def get_total_req_dict(self, howmany=1, extra_product_dict={}):
        self.make_child(howmany,extra_product_dict)
        return self.total_req_dict

    def is_has_child(self):
        if self.children == {}:
            return False
        else:
            return True
