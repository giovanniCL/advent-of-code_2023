def use_memo(func):
    memo = {}
    def wrapper(key):
        value = memo.get(key)
        if not value:
            value = func(key)
        memo[key] = value
        return value
    return wrapper
