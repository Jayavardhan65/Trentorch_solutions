def is_truthy(value) -> bool:
    if value is None:
        return False
    elif isinstance(value,(int,float,complex)):
        return value!=0
    elif isinstance(value,str):
        return len(value)>0
    elif isinstance(value,(list,tuple,set,dict)):
        return len(value)>0
    """
    Return the truthiness of `value` exactly as Python's own
    rules would determine it (equivalent to bool(value), but
    implement the logic explicitly rather than calling bool()
    directly, handle None, numbers, strings, lists, tuples,
    dicts, and sets).
    """
    pass


def first_truthy(values: list):
    for value in values:
        if is_truthy(value):
            return value
    return None
    """
    Return the first value in `values` that is truthy. If no
    value in the list is truthy, return None.
    Do not use Python's built-in `any()`, implement the scan
    explicitly using is_truthy-style checks.
    """
    pass
