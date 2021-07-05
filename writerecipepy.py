import json
import luarecipecopy
lcc=luarecipecopy.Copyrecipe()
# 가독성, 외부 에디터를 이용한 수동 편집을 고려하여 json과 유사한 형태로 딕셔너리 파일 생성
towrite='recipe = '+json.dumps(lcc.final(),sort_keys=False,indent=4)+'\n'
with open('recipe.py','w') as recipe:
    recipe.write(towrite)