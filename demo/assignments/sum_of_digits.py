num = int(input("Enter a number :"))

total = 0
num = abs(num)  # Get absolute value

while num > 0:
    digit = num % 10  # Take rightmost digit
    total += digit
    num //= 10  # Remove rightmost digit

print("Total ", total)
