
total = 0
for i in range(5):
    try:
        num = int(input("Enter a number :"))
        total += num
    except ValueError as ex:
        print("Invalid Number. Error -->", ex)

print("Total", total)

