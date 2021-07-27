import json


def write(dict_obj: dict, dict_name: str, directory: str):
    towrite = json.dumps(dict_obj, sort_keys=False, indent=4)
    towrite = dict_name + ' = ' + towrite + '\n'
    towrite = towrite.replace('true', 'True').replace('false', 'False').replace('null', 'None').replace('"',"'")
    with open(directory, 'w') as outf:
        outf.write(towrite)
    print(dict_name + ' converted to ' + directory)
