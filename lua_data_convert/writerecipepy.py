import json
import luarecipeconvert
from converted_data import dict_merge

lcc = luarecipeconvert.Copyrecipe()
# 가독성, 외부 에디터를 이용한 수동 편집을 고려하여 json과 유사한 형태로 딕셔너리 파일 생성
#towrite = 'recipe = ' + json.dumps(lcc.final(), sort_keys=False, indent=4) + '\n'
towrite1= dict_merge.Merger()
towrite = 'recipe_info = ' + json.dumps(towrite1.merge(), sort_keys=False, indent=4) + '\n'
with open('../converted_data/recipe_info.py', 'w') as recipe:
    recipe.write(towrite)
