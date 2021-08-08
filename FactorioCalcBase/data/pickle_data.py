import pickle
import pprint
from module_modifier_dict import module_modifier_dict
from production_machine_dict import production_machine_dict
from productivity_module_available_list import productivity_module_available_list
from recipe_dict import recipe_dict
from production_machine_category_list_dict import production_machine_category_list_dict
from sorted_recipe_list import sorted_recipe_list


def pickle_data():
    pdata = {
        'production_machine_dict': production_machine_dict,
        'module_modifier_dict': module_modifier_dict,
        'production_machine_category_list_dict': production_machine_category_list_dict,
        'recipe_dict': recipe_dict,
        'productivity_module_available_list': productivity_module_available_list,
        'sorted_recipe_list': sorted_recipe_list
    }

    with open('data_dict.pickle', 'wb') as pk:
        pickle.dump(pdata, pk)


pickle_data()

with open('data_dict.pickle', 'rb') as pk:
    dataaa = pickle.load(pk)

pprint.pp(dataaa)
