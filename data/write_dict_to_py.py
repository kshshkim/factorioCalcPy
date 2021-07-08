import json


class WriteDictToPy:

    @classmethod
    def write(self, dict_obj, dict_name: str, directory):
        towrite = json.dumps(dict_obj, sort_keys=False, indent=4)
        towrite = dict_name + ' = ' + towrite + '\n'
        towrite = towrite.replace('true', 'True').replace('false', 'False').replace('null', 'None')
        with open(directory, 'w') as outf:
            outf.write(towrite)
        print(dict_name + ' converted to ' + directory)
