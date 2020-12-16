def fun(a, b):
    print(id(a), id(b))


def set_zero(n):
    n = 0


# x = 10
# y = 20
# print(id(x), id(y))
# fun(x, y)

v = 100
set_zero(v)
print(v)
