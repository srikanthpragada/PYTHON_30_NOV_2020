def iseven(n):
    return n % 2 == 0


def ispositive(n):
    return n > 0


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact


# Execute the code only when run as script
if __name__ == '__main__':
    print(iseven(10))
    print(ispositive(-10))
    print(factorial(6))
else:  # code to execute when module is imported
    pass
