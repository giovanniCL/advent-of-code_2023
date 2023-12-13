def use_memo_with_lists(func):
    memo = {}
    def wrapper(list_1, list_2):
        key = (tuple(list_1), tuple(list_2))
        value = memo.get(key)
        if not value:
            value = func(list_1, list_2)
            memo[key] = value
        return value
    return wrapper