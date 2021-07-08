from slpp import slpp as lua
import json
itemlua=open('item.lua', 'r')
stritemlua=str(itemlua.read())
itemlua.close()


class Itemg:

    def lua_parse(self):
        itemstr = stritemlua.split('\n  },\n  {')
        returndict={}
        for itemblockstr in itemstr:
            itemblockstr = '  {' + itemblockstr + '\n  },'
            itemdict = lua.decode(itemblockstr)
            returndict[itemdict['name']]=itemdict
        return returndict

asdf=Itemg()

print(json.dumps(asdf.lua_parse(), sort_keys=False, indent=6))

towrite=json.dumps(asdf.lua_parse(), sort_keys=False, indent=4)
towrite='item_info = '+towrite+'\n'
towrite=towrite.replace('true','True').replace('false','False')
open('../item_info.py', 'w').write(towrite)