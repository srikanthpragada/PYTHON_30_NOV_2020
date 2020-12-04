# Accept a number and display its factors except 1 and itself

num = int(input("Enter number :"))

for i in range(2, num//2 + 1):
    if num % i == 0:
        print(i)

