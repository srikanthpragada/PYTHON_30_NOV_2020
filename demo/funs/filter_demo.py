# Takes a string and returns True or False
def large_name(s):
    return len(s) > 5

def has_special_char(s):
    for c in s:
        if not c.isalnum():
            return True

    return False

names = ['Java', 'C++', 'Python', 'JavaScript', 'C#']

for n in filter(large_name, names):
    print(n)

for n in filter(has_special_char, names):
    print(n)
