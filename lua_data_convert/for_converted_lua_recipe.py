import lua_data_converter
import pprint

ldc = lua_data_converter.LuaConverter()

pprint.pp(ldc.parse('recipe1.lua'))
