import os
import sys


def has_string(filename, st):
    try:
        with open(filename, "rt") as file:
            return st in file.read()
    except:
        pass


if len(sys.argv) < 3:
    print("Usage : search_python_files.py  startdir searchstring")
    exit(1)

files_generator = os.walk(sys.argv[1])
search = sys.argv[2]

for (dirname, folders, files) in files_generator:
    for file in files:
        filename = dirname + "\\" + file
        if filename.endswith(".py"):
            if has_string(filename, search):
                print(filename)
