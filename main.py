import json
from factorio_item_class import FactorioItem


class Test():
    def jprint(self, obj):
        print(json.dumps(obj, sort_keys=False, indent=6))


tst = Test()
asdfa = FactorioItem('processing-unit')
print('총 아이템 요구량')
tst.jprint(asdfa.get_total_req_dict())
print('')