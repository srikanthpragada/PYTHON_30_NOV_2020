def mathop(a, b, op):
    return op(a, b)


def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


result = mathop(10, 20, add)
