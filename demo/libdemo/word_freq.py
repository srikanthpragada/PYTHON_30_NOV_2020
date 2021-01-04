import re

file = open(r"c:\classroom\old_man.txt","rt")
words = re.findall(r"\w+", file.read())
file.close()

for w in sorted(set(words)):
    print(f"{w:15}   {words.count(w)}")