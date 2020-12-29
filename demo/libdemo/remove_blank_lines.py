# Remove blank lines

# Open file in read mode and read all non-blank lines into list
lines = []
f = open("names.txt", "rt")
for line in f.readlines():
    if len(line.strip()) > 0:  # non-blank line
        lines.append(line)

f.close()

# Write lines back to file
f = open("names.txt", "wt")
for line in sorted(lines):
    f.write(line)

f.close()
