import json
from FactorioCalcBase.legacy import lua_recipe_converter
from data import dict_merge

lcc = lua_recipe_converter.Copyrecipe()
# 가독성, 외부 에디터를 이용한 수동 편집을 고려하여 json과 유사한 형태로 딕셔너리 파일 생성
# towrite = 'recipe_dict = ' + json.dumps(lcc.final(), sort_keys=False, indent=4) + '\n'
towrite1 = dict_merge.Merger()
towrite = 'recipe_dict = ' + json.dumps(towrite1.merge(), sort_keys=False, indent=4) + '\n'
with open('data/recipe_dict.py', 'w') as recipe:
    recipe.write(towrite)
