import dependencydictbuilder
import json
from factorioItemclass import factorioItem


class Test():
    def jprint(self, obj):
        print(json.dumps(obj, sort_keys=False, indent=6))





tst = Test()
asdfa=factorioItem('processing-unit')
print('processing-unit 총 아이템 요구량')
tst.jprint(asdfa.gettotalrequirements())