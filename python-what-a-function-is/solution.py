def is_even(n: int) -> bool:
    if (n%2==0):
        return True
    else:
        return False
    """
    Return True if n is even, False otherwise.
    """
    pass


def greet_formal(name: str, title: str) -> str:
    return f"Good day, {title} {name}." 
    """
    Return a greeting string in the exact form:
      "Good day, {title} {name}."
    Example: greet_formal("Smith", "Dr.") -> "Good day, Dr. Smith."
    """
    pass


def apply_twice(func, value):
    result = func(value)
    result = func(result)
    return result
    """
    Call `func` on `value`, then call `func` again on the result
    of that first call. Return the final result.
    Example: apply_twice(lambda x: x + 1, 5) -> 7
    """
    pass
