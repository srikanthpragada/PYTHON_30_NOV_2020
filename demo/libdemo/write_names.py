names = ["Greg", "Larry", "Mark", "Bill", "Steve", "Elon"]
f = open("names.txt", "wt")
for n in names:
    f.write(n + "\n")

f.close()
