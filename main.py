import dependencydictbuilder
import json


class Test():
    def jprint(self, obj):
        print(json.dumps(obj, sort_keys=False, indent=6))


tst = Test()
ddb = dependencydictbuilder.DependencyDictBuilder()
tst.jprint(ddb.dependencyFinder_dict('processing-unit'))
