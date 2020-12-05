total = count = 0
while True:
    num = int(input("Enter marks [0 to stop] :"))
    if num == 0:
        break  # Stop loop

    if num < 0:
        continue  # Start next iteration

    total += num
    count += 1

print("Average = ", total / count)


