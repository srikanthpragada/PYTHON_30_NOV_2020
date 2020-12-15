def greet(message='Hello', *names):
    for n in names:
        print(f"{message} {n}")


def wish(*names, message="Hi"):
    pass


greet('Hi', 'Steve', 'Bob')
wish("abc", "xyz", message="Hello")
