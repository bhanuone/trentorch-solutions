def is_truthy(value) -> bool:
    """
    Return the truthiness of `value` exactly as Python's own
    rules would determine it (equivalent to bool(value), but
    implement the logic explicitly rather than calling bool()
    directly, handle None, numbers, strings, lists, tuples,
    dicts, and sets).
    """
    t = type(value).__name__
    if value == None or value == False:
        return False
    elif value == True:
        return True
    elif t == 'int' or t == 'float':
        return value != 0
    else:
        return len(value) > 0
        


def first_truthy(values: list):
    """
    Return the first value in `values` that is truthy. If no
    value in the list is truthy, return None.
    Do not use Python's built-in `any()`, implement the scan
    explicitly using is_truthy-style checks.
    """
    for v in values:
        if is_truthy(v):
            return v
