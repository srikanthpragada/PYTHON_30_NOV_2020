
num = 145
org_num = num

total = 0
while num > 0:
    digit = num % 10

    # Calculate factorial for digit
    fact = 1
    for i in range(2, digit + 1):
        fact *= i

    total += fact

    # remove rightmost digit
    num //= 10

if total == org_num:
    print("Strong number!")
else:
    print("Not a strong number!")


