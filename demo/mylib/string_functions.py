def hasdigit(s):
    for c in s:
        if c.isdigit():
            return True

    return False


def extract_digits(s):
    digits = [c for c in s if c.isdigit()]
    return "".join(digits)

