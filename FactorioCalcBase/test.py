from dependency_tracker import DependencyDictMerged
from calculator_base import FactorioCalculatorBase
import pprint
from production_block import ProductionBlock

pprint.pp = pprint.pprint
ddd = FactorioCalculatorBase('processing-unit')
# pprint.pp(ddd.block_obj_dict)
ddd.set_module_to_specific_block('advanced-circuit',['p3','p1','s3'])
# print(ddd.general_obj_dict['advanced-circuit'].module_list)
# print(ddd.general_obj_dict['advanced-circuit'].production_speed)
# print(ddd.general_obj_dict['advanced-circuit'].power_consumption)
#
#
# print(ddd.resource_consumption_dict)
# print(ddd.update_total_recipe_dict())
#
# pprint.pp('eaeas')
#
# pprint.pp(asdf.merged_item_dict)
# pprint.pp(asdf.merged_recipe_dict)
# pprint.pp(asdf.merged_gen_dict)
# pprint.pp(asdf.merged_oil_dict)
print(ddd.json_out())
pprint.pp(ddd.total_item_dict)
