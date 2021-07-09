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

    def makechild(self, ancestors_needs=1.0):  # TODO totalreqdict 메소드 분리하기
        self.children = {}
        self.ingredientsperone = self.getingredientsperone()
        amount_ancestors_needs = copy.deepcopy(ancestors_needs)
        if self.ingredients != '':
            for key in self.ingredients.keys():
                child = FactorioItem(key)
                child.mother = self
                child.amount_mother_needs = float(self.ingredientsperone[key])
                child.amount_ancestors_needs = child.amount_mother_needs * amount_ancestors_needs
                self.children[child.name + ' *' + str(child.amount_ancestors_needs)] = child  # self.children.values() <- children 목록,
                # children 변수에 지정된 딕셔너리에 FactorioItem 타입 오브젝트를 value로 저장, list로 하는게 나을지 이게 나을지 아직 못 정함
                child.makechild(child.amount_ancestors_needs)

    def get_total_req_dict(self, howmany=1):  # 아이템 요구량 트리 순회
        self.amount_ancestors_needs = howmany
        self.makechild(howmany)
        current = self
        search_que = [self]
        total_req_dict = {}

        while search_que != []:
            for child in current.children.values():  # 큐에 차일드 전부 추가
                search_que.append(child)

            if total_req_dict.get(current.name) == None:  # total_req_dict에 self.name과 일치하는 key가 없으면 추가
                total_req_dict[current.name] = 0

            total_req_dict[current.name] = total_req_dict[current.name] + current.amount_ancestors_needs

            search_que.pop(0)  # 큐에서 self 제거
            if search_que != []:
                current = search_que[0]  # current 변경

        return total_req_dict

    def is_has_child(self):
        if self.children == {}:
            return False
        else:
            return True

    def gettotalrequirements(self):
        self.makechild()
        return self.totalreqdict
