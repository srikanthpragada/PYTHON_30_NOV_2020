import sys

# Whether command line argument is passed
if len(sys.argv) < 2:
    print("Usage : python prime_number.py number")
    exit(0)

num = int(sys.argv[1])  # Convert 1st command line argument to int

for i in range(2, num//2 + 1):
    if num % i == 0:
        print("Not a prime!")
        break
else:
    print("Prime Number!")

