from FactorioCalcBase.data.binary import recipe_dict


def get_recipe_list():
    new_list = list(recipe_dict.keys())
    return new_list


def get_recipe(recipe_name: str):
    target = recipe_dict[recipe_name]
    return target
