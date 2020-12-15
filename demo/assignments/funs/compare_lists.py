def are_equal(lst1, lst2):
    # False if lists have different sizes
    if len(lst1) != len(lst2):
        return False

    # Return false if any corresponding elements do not match
    for v1, v2 in zip(lst1, lst2):
        if v1 != v2:
            return False

    return True


l1 = [1, 2, 3, 4, 5]
l2 = [1, 1, 3, 4, 5]

print(are_equal(l1, l2))
