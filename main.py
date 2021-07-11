import json
from factorio_calc_class import FactorioCalc
from factorio_item_class import FactorioItem


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

fcfc=FactorioCalc('processing-unit')
print(fcfc.get_available_machine_list())
fcfc.update_machine('assembling-machine-3')
fcfc.add_a_module('s1')
fcfc.add_a_module('s2')
fcfc.add_a_module('p1')
fcfc.add_a_module('p3')
print(fcfc.machine_obj.total_modifier)
print(fcfc.machine_obj.resource_consumption_rate)
print(fcfc.production_machine_name)
print(fcfc.to_add_module_list)
print(fcfc.machine_obj.total_modifier)
tst.jprint(fcfc.item_obj.get_total_req_dict())
print()