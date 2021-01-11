import sqlite3

con = sqlite3.connect(r"c:\classroom\nov30p\hr.db")
cur = con.cursor()
f = open("employees.txt", "rt")
ef = open("errors.txt","wt")
count = 0
for line in f.readlines():
    try:
        line = line.strip()
        if len(line) == 0:
            continue

        name, job, salary = line.split(",")
        cur.execute("insert into employees(name,job,salary) values(?,?,?)", (name, job, salary))
        count += 1
    except Exception as ex:
        ef.write(f"Error : {ex}  Line : {line.strip()}\n")

con.commit()
print(f"Loaded {count} employees!")
cur.close()
con.close()
ef.close()
