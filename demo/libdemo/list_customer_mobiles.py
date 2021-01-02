import re

file = open("customers.txt", "rt")
mobiles = []
for line in file.readlines():
    match = re.search(r'\d+', line)
    if match is not None:
        number = match.group(0)
        if len(number) == 10:
            mobiles.append(number)

file.close()

print(mobiles)
