marks = "90,88,77,xyz,68,,78,46,88,33,56,abc"
print(sum([int(m) for m in marks.split(",") if m.isdigit()]))
