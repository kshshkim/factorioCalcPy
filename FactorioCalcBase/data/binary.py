# 파이썬이 매번 스크립트에서 객체를 재생성하는지 여부를 몰라서 pickle 모듈로 바이너리화함.
import pickle
with open('FactorioCalcBase/data/data_dict.pickle', 'rb') as pk:
    dataaa = pickle.load(pk)
recipe_dict = dataaa['recipe_dict']
production_machine_category_list_dict = dataaa['production_machine_category_list_dict']
production_machine_dict = dataaa['production_machine_dict']
module_modifier_dict = dataaa['module_modifier_dict']
productivity_module_available_list = dataaa['productivity_module_available_list']
sorted_recipe_list = dataaa['sorted_recipe_list']

# from FactorioCalcBase.data.module_modifier_dict import module_modifier_dict
# from FactorioCalcBase.data.production_machine_dict import production_machine_dict
# from FactorioCalcBase.data.productivity_module_available_list import productivity_module_available_list
# from FactorioCalcBase.data.recipe_dict import recipe_dict
# from FactorioCalcBase.data.production_machine_category_list_dict import production_machine_category_list_dict
# from FactorioCalcBase.data.sorted_recipe_list import sorted_recipe_list
#
