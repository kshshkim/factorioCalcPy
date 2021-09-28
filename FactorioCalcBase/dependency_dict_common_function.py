import copy
from collections import Counter, deque
from FactorioCalcBase.recipe_class import RecipeClass


def find_recipe(needed_list, extra_product_rate_dict):
    item_name = needed_list[0]
    item_amount = needed_list[1]

    if item_name in ['petroleum-gas', 'light-oil', 'heavy-oil', 'uranium-235', 'uranium-238']:
        return -1
    elif item_name == 'solid-fuel':  # TODO solid-fuel,
        recipe_name = 'solid-fuel-from-light-oil'
        trc = RecipeClass(recipe_name)
    else:
        recipe_name = item_name
        trc = RecipeClass(recipe_name)

    extra_product_rate = extra_product_rate_dict.get(recipe_name)
    if extra_product_rate is None:
        extra_product_rate = 1

    recipe_amount = item_amount / (trc.get_results_count() * extra_product_rate)
    if recipe_name != '' and recipe_amount != 0:
        return [recipe_name, recipe_amount]


def construct_dependency_dict(recipe_name: str, recipe_amount: float, extra_product_rate_dict: dict):
    recipe_obj = RecipeClass(recipe_name, recipe_amount)

    obj_search_queue = deque([recipe_obj])
    item_needed_queue = deque([])
    cannot_process_item_dict = {}
    total_recipe_needed_dict = {recipe_obj.name: recipe_obj.amount}
    total_item_needed_dict = {}

    while obj_search_queue:
        current = obj_search_queue[0]
        if current.ingredients != '':
            for key, val in current.ingredients.items():
                to_append = [key, val * current.amount]
                item_needed_queue.append(to_append)
                add_to_item_dict(total_item_needed_dict, item_name=key, item_amount=val * current.amount,
                                 required_by=current.name)

        while item_needed_queue:  # [0] = current, [][0] = name [][1] = amount
            found_recipe = find_recipe(item_needed_queue[0], extra_product_rate_dict)

            if found_recipe == -1:
                # item_needed_queue[0][b], 0: index, b:0: item name, b:1: item amount
                item_name = item_needed_queue[0][0]
                item_amount = item_needed_queue[0][1]
                dict_add_number(cannot_process_item_dict, key=item_name, val=item_amount)
            else:
                returned = find_recipe(item_needed_queue[0], extra_product_rate_dict)
                # returned, [0]: name, [1]: amount
                new_rcp_obj = RecipeClass(returned[0], amount=returned[1])
                dict_add_number(total_recipe_needed_dict, key=returned[0], val=returned[1])
                obj_search_queue.append(new_rcp_obj)
            item_needed_queue.popleft()
        obj_search_queue.popleft()

    return [total_recipe_needed_dict, total_item_needed_dict, cannot_process_item_dict]


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
