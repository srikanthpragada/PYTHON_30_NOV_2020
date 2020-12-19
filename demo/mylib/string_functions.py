def hasdigit(s):
    """
    hasdigit(str) -> bool

    Returns true if given string has a digit

    """
    for c in s:
        if c.isdigit():
            return True

    return False


def extract_digits(s):
    digits = [c for c in s if c.isdigit()]
    return "".join(digits)

