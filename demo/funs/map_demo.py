def next_even(n):
    return n + 2 if n % 2 == 0 else n + 1


nums = [1, 5, 4, 2, 3, 8]
names = ['Java', 'C++', 'Python', 'JavaScript', 'C#']

# for n in map(next_even, nums):
#     print(n)

for n in map(len, names):
    print(n)
