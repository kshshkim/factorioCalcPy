from FactorioCalcBase.data.binary import recipe_dict


def get_recipe_list():
    rclist = list(recipe_dict.keys())
    toreturnlist = []

    for itm in rclist:
        new_dict = {
            'name': itm,
            'id': itm
        }
        toreturnlist.append(new_dict)

    return toreturnlist
