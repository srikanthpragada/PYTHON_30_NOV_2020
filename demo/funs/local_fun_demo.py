g = 100  # Global variable


def f1():
    global g
    g = 101
    e = 200  # Enclosing variable

    # Local function
    def f2():
        nonlocal e
        l = 300  # Local variable
        e = 20
        print("local function")
        print(l, e, g)

    print("In f1()")
    f2()
    print(e)


f1()
