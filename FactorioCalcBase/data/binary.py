import pickle
with open('data/data_dict.pickle', 'rb') as pk:
    dataaa = pickle.load(pk)
recipe_dict = dataaa['recipe_dict']
production_machine_category_list_dict = dataaa['production_machine_category_list_dict']
production_machine_dict = dataaa['production_machine_dict']
module_modifier_dict = dataaa['module_modifier_dict']
productivity_module_available_list = dataaa['productivity_module_available_list']
