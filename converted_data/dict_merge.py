from converted_data.recipe_info import recipe_info
from converted_data.item_info import item_info
from converted_data.fluid_info import fluid_info
import copy

# factorio의 제조법/아이템 데이터 파일은 item.lua와 fluid.lua, recipe.lua 등으로 나뉘어있음. 계산기 구현할때는 합치는게 더 간결

class Merger:
    def merge(self):
        toreturnrecipe=copy.deepcopy(recipe_info)
        for key in toreturnrecipe:
            if fluid_info.get(key) is not None:
                toreturnrecipe[key]['subgroup']='fluid'
                toreturnrecipe[key]['icon']=fluid_info[key]['icon']
            elif item_info.get(key) is not None:
                toaddlist=['icon','subgroup'] # item_info.py에서 필요한 정보만
                for toadd in toaddlist:
                    if item_info[key].get(toadd) is not None:
                        toreturnrecipe[key][toadd]=item_info[key][toadd]
        return toreturnrecipe
