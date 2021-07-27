from FactorioCalcBase.data.binary import *


def get_recipe_spec(recipe_name: str):
    target = recipe_dict.get(recipe_name)
    return target


def get_recipe_list():
    target = list(recipe_dict.keys())
    return target


def get_machine_spec(machine_name: str):
    target = production_machine_dict.get(machine_name)
    return target


def get_machine_list(category: str):
    target = production_machine_category_list_dict.get(category)
    return target


def is_production_module_available(recipe_name: str):
    if recipe_name in productivity_module_available_list:
        return True
    else:
        return False


def what_machine_can_produce(recipe_name: str):
    recp = recipe_dict.get(recipe_name)
    if recp is None:
        return 'wrong name or server error'
    else:
        cat = recp.get('category')

    if cat is None:
        cat = 'crafting'
    return cat

