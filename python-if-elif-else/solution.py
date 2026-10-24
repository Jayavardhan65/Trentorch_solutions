def classify_number(x: int | float) -> str:
    if x < 0:
        return "negative"
    elif x == 0:
        return "zero"
    elif 0<x<=10:
        return "small"
    elif x > 10:
        return "large"
    """
    Return one of the following strings based on x, checked in
    this exact order using an if/elif/else chain:
      "negative"     if x < 0
      "zero"         if x == 0
      "small"        if 0 < x <= 10
      "large"        if x > 10
    """
    pass
