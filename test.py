import json
from factorio_production_block_class import FactorioProductionBlock
from factorio_item_class import FactorioItem
from f_calc_main import FactorioCalcBody

class Test():
    def jprint(self, obj):
        print(json.dumps(obj, sort_keys=False, indent=6))


resource_consumption_dict = {
    # 'processing-unit': 0.9090909,
    # 'advanced-circuit': 0.85

}

tst = Test()
# asdfa = FactorioItem('processing-unit')
# print('총 아이템 요구량')
# tst.jprint(asdfa.get_total_req_dict())
# print('')

fcfc=FactorioProductionBlock('advanced-circuit')
# print(fcfc.get_available_machine_list())
# fcfc.update_machine('assembling-machine-3')
# fcfc.add_a_module('s1')
# fcfc.add_a_module('s2')
# fcfc.add_a_module('p1')
# fcfc.add_a_module('p3')
# print(fcfc.machine_obj.total_modifier)
# print(fcfc.machine_obj.resource_consumption_rate)
# print(fcfc.production_machine_name)
# print(fcfc.to_add_module_list)
# print(fcfc.machine_obj.total_modifier)
# tst.jprint(fcfc.item_obj.get_total_req_dict())
# print()

fcb = FactorioCalcBody(main_item_name='processing-unit',machine_amount=1)
fcb.main_block_obj.add_a_module('e3')
# fcb.main_block_obj.add_a_module('s3')
# fcb.main_block_obj.add_a_module('s3')
fcb.main_block_obj.update_machine(machine_name='assembling-machine-2', module_list=[])
tst.jprint(fcb.get_total_calculated_dict())

# fcb.main_block_obj.add_a_module('p3')
# fcb.main_block_obj.add_a_module('s3')
# print(fcb.main_block_obj.to_add_module_list)
# print(fcb.main_block_obj.machine_obj.total_modifier)
# fcb.block_objs_dict['copper-cable'].add_a_module('p1')
#
#fcb.update_resource_consumption_rate_dict()
# fcb.update_resource_consumption_rate_dict()
# fcb.make_ingredient_block_objs()
# # print(fcb.resource_consumption_rate_dict)
#
# fcb.update_total_req_dict()
# fcb.build_dict_total_calculated()
# tst.jprint(fcb.build_dict_total_calculated())