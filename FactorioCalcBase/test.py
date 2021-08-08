def dict_add_number(dic: dict, key, val: float):
    if dic.get(key) is None:
        dic[key] = val
    else:
        dic[key] += val



asdf = {
    'apple': 1
}

dict_add_number(asdf, 'apple', 1)

print(asdf)