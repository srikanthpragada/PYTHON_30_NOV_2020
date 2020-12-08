st = "How do you do today?"

for c in st:
    if c == ' ':    # ord(c) == 32
        print()  # Go to next line
    else:
        print(c, end='')

