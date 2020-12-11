nums = []

for i in range(1, 6):
    num = int(input("Enter a number :"))
    if num not in nums:  # Ignore duplicate number
        nums.append(num)


print(nums)