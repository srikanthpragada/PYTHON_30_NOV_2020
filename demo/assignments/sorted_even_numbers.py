numbers = []

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break
    numbers.append(num)

numbers.sort()

for num in numbers:
    if num % 2 == 0:
        print(num)

