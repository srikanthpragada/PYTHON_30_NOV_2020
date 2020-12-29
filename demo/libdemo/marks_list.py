try:
    f = open("marks.txt", "rt")
    students = []
    for line in f.readlines():
        parts = line.strip().split(",")
        name = parts[0]
        # Convert marks which are in the form strings to ints
        marks = [int(v) for v in parts[1:]]
        total = sum(marks)
        students.append((name, parts[1:], total, total / len(marks)))

    for name, marks, total, avg in sorted(students, key=lambda s: s[2], reverse=True):
        print(f"{name:20} {','.join(marks):15} {total:3} {avg:5.2f}")

except Exception as ex:
    print("Error -> ", ex)
