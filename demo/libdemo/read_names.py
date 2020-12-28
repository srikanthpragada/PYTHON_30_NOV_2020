f = open("names.txt", "rt")
for n in f.readlines():
    print(n.strip())   # Strip whitespace

f.close()
