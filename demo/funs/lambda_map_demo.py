nums = [1, 5, 4, 2, 3, 8]
names = ['Java', 'C++', 'Python', 'JavaScript', 'C#']

for n in map(lambda v: v + 2 if v % 2 == 0 else v + 1, nums):
    print(n)

for n in map(lambda n: n[0] + n[-1], names):
    print(n)
