from data.recipe_dict import recipe_dict
from data.item_dict import item_dict
from data.fluid_dict import fluid_dict
import copy


# factorio의 제조법/아이템 데이터 파일은 item.lua와 fluid.lua, recipe_dict.lua 등으로 나뉘어있음. 계산기 구현할때는 합치는게 더 간결

class Merger:
    def merge(self):
        toreturnrecipe = copy.deepcopy(recipe_dict)
        for key in toreturnrecipe:
            if fluid_dict.get(key) is not None:
                toreturnrecipe[key]['subgroup'] = 'fluid'
                toreturnrecipe[key]['icon'] = fluid_dict[key]['icon']
            elif item_dict.get(key) is not None:
                toaddlist = ['icon', 'subgroup']  # item_dict.py에서 필요한 정보만
                for toadd in toaddlist:
                    if item_dict[key].get(toadd) is not None:
                        toreturnrecipe[key][toadd] = item_dict[key][toadd]
        return toreturnrecipe
