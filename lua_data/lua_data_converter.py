from slpp import slpp as lua
import json


class LuaConverter:
    def parse(self, luafile):
        with open(luafile, 'r') as to_convert:
            to_convert = str(to_convert.read())
        to_convert = to_convert.replace('data:extend(\n{\n  {', '').replace('})\n', '')  # slpp가 알아먹을수 있는 형태로 가공
        to_convert = to_convert.replace('  },\n\n', '  },\n')  # 불규칙적으로 두 칸 띄운 경우가 있음.
        item_info_list = to_convert.split('\n  },\n  {')
        returndict = {}
        for each_item in item_info_list:  # 아이템별로 따로 반복
            each_item = '  {' + each_item + '\n  },'
            each_item_dict = lua.decode(each_item)  # lua 데이터 변환 라이브러리 slpp 사용
            returndict[each_item_dict['name']] = each_item_dict  # 딕셔너리 하위에 slpp가 return한 딕셔너리 삽입
        return returndict

    def write(self, infile, outfile):
        towrite = json.dumps(self.parse(infile), sort_keys=False, indent=4)
        towrite = infile.replace('.lua', '') + '_info = ' + towrite + '\n'
        towrite = towrite.replace('true', 'True').replace('false', 'False')
        outfilefulld = '../data/' + outfile
        with open(outfilefulld, 'w') as outf:
            outf.write(towrite)
        print(infile + ' converted to ' + outfilefulld)


'''
사용법

lc=LuaConverter()

lc.write('fluid.lua','fluid_dict.py')
'''
