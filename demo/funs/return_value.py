def add(n1, n2):
    return n1 + n2


def next_odd(num):
    return num + 1 if num % 2 == 0 else num + 2


def next_even(num):
    if num % 2 == 0:
        return num + 2
    else:
        return num + 1

    print('The End')


def count_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1

    return count


total = add(10, 20)
print(next_even(10))
print(count_even([10, 11, 15, 20, 40, 55]))
