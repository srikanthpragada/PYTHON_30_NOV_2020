import os

files_generator = os.walk(r"c:\classroom\nov30p")

for (dirname, folders, files) in files_generator:
    for file in files:
        if file.endswith(".py"):
            print(dirname + "\\" + file)
