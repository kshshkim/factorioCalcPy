import copy
from collections import Counter


def dict_add_number(dic: dict, key, val: float):
    if dic.get(key) is None:
        dic[key] = val
    else:
        dic[key] += val


def counter_add_dict(dict_list: list, prefix: str = ''):
    counter_obj = Counter({})
    for each_dict in dict_list:
        counter_obj += Counter(each_dict)
    to_return_dict = {
        prefix: dict(counter_obj)
    }
    return to_return_dict


def add_to_item_dict(base_dict: dict, item_name: str, item_amount: float, required_by: str):

    # item_dict = {
    #     item_name :{
    #         'amount': float,
    #         'required_by': {
    #             recipe_1: float,
    #             recipe_2: float
    #         }
    #     }
    # }

    if base_dict.get(item_name) is None:
        base_dict[item_name] = {
            'name': item_name,
            'amount': item_amount,
            'required_by': {
                required_by: item_amount
            }
        }
    else:
        base_dict[item_name]['amount'] += item_amount
        dict_add_number(base_dict[item_name]['required_by'], required_by, item_amount)


def merge_item_dicts(dict_list):
    to_return: dict = copy.deepcopy(dict_list[0])
    sub_dict = dict_list[1]
    for key in sub_dict.keys():
        if key in to_return.keys():
            small_dict1 = to_return[key]
            small_dict2 = sub_dict[key]
            small_dict1['amount'] += small_dict2['amount']
            required_by_base = Counter(to_return[key]['required_by'])
            required_by_add = Counter(sub_dict[key]['required_by'])
            to_return[key]['required_by'] = dict(required_by_base+required_by_add)
        else:
            to_return[key] = sub_dict[key]
    return to_return
