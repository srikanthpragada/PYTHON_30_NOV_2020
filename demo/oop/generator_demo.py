# Generator
def numbers():
    for n in range(1, 10):
        yield n


nums = numbers()
print(type(nums))
print(next(nums))
print(next(nums))
# for n in nums:
#     print(n)
