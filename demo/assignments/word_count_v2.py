# python word_count.py  filename

import sys

if len(sys.argv) < 2:
    print("Usage : python word_count.py <filename> ... ")
    exit(0)

for filename in sys.argv[1:]:
    try:
        with open(filename, "rt") as file:
            lines = words = chars = 0

            for line in file.readlines():
                lines += 1
                words += len(line.split())
                chars += len(line)

            print(f"{filename:20} Chars = {chars}, Words = {words}, Lines = {lines}")
    except Exception as ex:
        print(f"Error : ", ex)
