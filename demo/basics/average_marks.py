total = count = 0
while True:
    num = int(input("Enter marks [-1 to stop] :"))
    if num == -1:
        break  # Stop loop

    total += num
    count += 1

print("Average = ", total / count)


