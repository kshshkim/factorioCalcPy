from dependency_tracker import DependencyDictMerged

import pprint
from production_block import ProductionBlock

asdf = DependencyDictMerged(recipe_name='processing-unit')
aaaa = ProductionBlock(recipe_name='processing-unit')
# # print(asdf.get_total_recipe_req_dict())
# pprint.pprint(asdf.total_needed_item())
# pprint.pp(asdf.merged_oil_dict)
# pprint.pp(asdf.merged_recipe_dict)
# pprint.pp(asdf.merged_item_dict)
aaaa.set_module(['s1', 's2', 'p3', 'p2'])
# aaaa.get_total_modifier()
print(aaaa.module_list)
aaaa.update_machine('assembling-machine-2')
print(aaaa.module_list)
pprint.pprint(aaaa.total_modifier)
#
# pprint.pp('eaeas')
#
# pprint.pp(asdf.merged_item_dict)
# pprint.pp(asdf.merged_recipe_dict)
# pprint.pp(asdf.merged_gen_dict)
# pprint.pp(asdf.merged_oil_dict)
