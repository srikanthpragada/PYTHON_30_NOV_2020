def count_upper(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1

    return count


print(count_upper("ABCxyzPqr"))
