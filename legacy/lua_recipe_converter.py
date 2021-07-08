import copy
import re
from ast import literal_eval

recipe = open('recipe.lua', 'r')
strrecipe = str(recipe.read())  # 문자열로
recipe.close()


class Copyrecipe:

    def recipeconvert(self):
        returndict = dict()
        strcopyrecipe = copy.deepcopy(strrecipe)
        strcopyrecipe = strcopyrecipe.replace('  },\n\n', '  },\n')
        iteminstrlist = strcopyrecipe.split('  },\n  {\n')
        for iteminstr in iteminstrlist:
            # remove useless infos
            iteminstr = iteminstr.replace('    enabled = false,\n', '')
            iteminstr = iteminstr.replace('    type = "recipe_dict",\n', '')

            # get name
            name = re.search('name = \".*\"', iteminstr).group()
            name = name.replace('name = "', '').replace('"', '')

            # TODO uranium-processing은 확률 요소가 들어있기 때문에 나중에 처리
            if name == 'uranium-processing':
                continue

            # get ptime
            energy_required = re.search('energy_required = .*,', iteminstr)
            if energy_required is None:  # energy_required가 없으면 0.5인 것으로 보임.
                energy_required = float(0.5)
            else:
                energy_required = energy_required.group()
                energy_required = energy_required.replace('energy_required = ', '').replace(',', '')
                energy_required = float(energy_required)
            # result와 ingredients를 얻기 위해 공백과 줄바꿈을 없앰
            iteminstr = iteminstr.replace('\n', '').replace(' ', '')

            # get pquant
            # result 혹은 results가 있음
            result = re.search('result=".*?"', iteminstr)
            results = None
            if result is not None:
                result = result.group()
                result = result.replace('result=', '')
                result_count = re.search('result_count=.*?[0-9]+', iteminstr)
                if result_count is None:
                    result_count = '1'
                else:
                    result_count = result_count.group().replace('result_count=', '')
                result = result + ':' + result_count
                result = '{' + result + '}'
                result = literal_eval(result)
            else:
                results = re.search('results={{.*?}}', iteminstr)
                results = results.group()
                results = results.replace('type=\"fluid\",name=', '').replace('type=\"item_dict\",name=', '')
                results = results.replace('{{', '{').replace('}}', '}')
                results = results.replace('results=', '')
                results = results.replace('",', '\':')
                results = results.replace('"', '\'')
                results = results.replace('amount=', '')
                results = results.replace('{', '').replace('}', '')
                results = '{' + results + '}'
                results = literal_eval(results)

            ingredients = re.search('ingredients=.*?\}\},', iteminstr)  # ?로 expensive 무시
            ingredients = ingredients.group().replace('ingredients=', '')

            ingredients = ingredients.replace('type=\"fluid\",name=', '')
            ingredients = ingredients.replace('type=\"item_dict\",name=', '')
            # 타입이 지정된 경우, 레시피 이름과 산출물 이름이 다른 것으로 보임.
            ingredients = ingredients.replace('amount=', '')
            ingredients = ingredients.replace('",', '\':')
            ingredients = ingredients.replace('\"', '\'')
            ingredients = ingredients.replace('{{', '#')
            ingredients = ingredients.replace('}},', '%')
            ingredients = ingredients.replace('}', '').replace('{', '')
            ingredients = ingredients.replace('#', '{').replace('%', '}')
            ingredients = literal_eval(ingredients)

            # get group

            # building dictionary
            returndict[name] = {}
            returndict[name]['name'] = name
            returndict[name]['energy_required'] = energy_required
            returndict[name]['ingredients'] = ingredients
            if result is not None:
                returndict[name]['results'] = result
            else:
                returndict[name]['results'] = results

        return returndict

    def checkitemexists(self):
        # 레시피 이름과 아이템 이름이 다르거나, 1차 재료라서 레시피가 존재하지 않는 경우 아이템 데이터를 생성, 추후 수정 필요
        asdict = cr.recipeconvert()
        noitemlist = list()
        for item in list(asdict.keys()):
            bsdict = asdict[item]['ingredients']
            for iitem in list(bsdict.keys()):
                if iitem not in list(asdict.keys()) and iitem not in noitemlist:
                    noitemlist.append(iitem)
        return (noitemlist)

    def makeDictinfo(self, returndict):
        # TODO 누락된 아이템 딕셔너리에 생성해야함. 아이템 종류에 따라서 다른 데이터 추가. 현재는 모두 raw인 것 처럼 처리.
        for item in self.checkitemexists():
            returndict[item] = {}
            returndict[item]['name'] = item
            returndict[item]['energy_required'] = ''
            returndict[item]['ingredients'] = ''
            returndict[item]['results'] = ''
        return returndict

    def final(self):
        return self.makeDictinfo(cr.recipeconvert())


cr = Copyrecipe()
