names = ['Java', 'C++', 'Python', 'JavaScript', 'C#']
nums = [-10, 10, 33, 44, -5, -6, 15]

for n in filter(lambda n: len(n) > 5, names):
    print(n)

for n in filter(lambda v: v >= 0, nums):
    print(n)
