from data.recipe_dict import recipe_dict
import copy


class FactorioItem:
    total_req_dict = dict
    children = dict

    def __init__(self, item_name: str, resource_consumption_rate_dict=None):

        self.name = item_name
        self.energy_required = recipe_dict[self.name]['energy_required']
        self.ingredients = recipe_dict[self.name]['ingredients']
        self.results = recipe_dict[self.name]['results']
        self.amount_ancestors_needs = 1
        self.category = self.get_category()
        self.ingredients_per_one = self.get_ingredients_per_one()
        self.energy_required_per_one = self.get_energy_required_per_one()
        if resource_consumption_rate_dict is None:
            resource_consumption_rate_dict = {}
        self.resource_consumption_rate_dict = resource_consumption_rate_dict

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

    def get_energy_required_per_one(self):
        try:
            if len(list(self.results.keys())) == 1:
                if float(self.results[self.name]) == 1.0:
                    return self.energy_required
                else:
                    return self.energy_required/float(self.results[self.name])
            else:
                pass
        except AttributeError: # results = '' 인 경우로, str 오브젝트임. 아직 미완성
            return 1 # 임시값

    def make_child(self, ancestors_needs=1.0):
        # 의존성 트리 생성, mother needs, ancestors needs 정보 전달, 총 아이템 요구량은 모든 객체들의 ancestors_needs 를 합하면 됨.

        self.amount_ancestors_needs = ancestors_needs
        self.total_req_dict = {}
        search_queue = [self]
        while search_queue != []:
            current = search_queue[0]
            current.children = {}
            if current.ingredients != '':
                for key in current.ingredients.keys():
                    child = FactorioItem(key)  # child obj 생성
                    child.mother = current
                    # 모디파이어 초기화, 기본 1
                    resource_consumption_modifier = float(1)

                    # 전달받은 딕셔너리에 값이 존재할 경우, 즉 생산모듈이 장착된 경우, current 의 1개당 아이템 요구량이 줄어드는 것으로 계산 가능.
                    if self.resource_consumption_rate_dict != {}:
                        if current.name in self.resource_consumption_rate_dict.keys():
                            resource_consumption_modifier = self.resource_consumption_rate_dict[current.name]

                    child.amount_mother_needs = float(current.ingredients_per_one[key]) * resource_consumption_modifier
                    child.amount_ancestors_needs = child.amount_mother_needs * current.amount_ancestors_needs

                    current.children[child.name] = child
                    search_queue.append(child)
            if self.total_req_dict.get(current.name) is None:  # total_req_dict 에 self.name 과 일치하는 key 가 없으면 추가
                self.total_req_dict[current.name] = 0
            self.total_req_dict[current.name] = self.total_req_dict[current.name] + current.amount_ancestors_needs

            search_queue.pop(0)

    def get_total_req_dict(self, howmany=1):
        self.make_child(howmany)
        return self.total_req_dict

    def is_has_child(self):
        try:
            if self.children == {} or self.children is None:
                return False
            else:
                return True
        except AttributeError:
            return False

    def get_category(self):
        try:
            return recipe_dict[self.name]['category']
        except KeyError:
            return 'crafting'
