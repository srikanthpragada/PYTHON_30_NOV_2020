import sqlite3

con = sqlite3.connect(r"c:\classroom\nov30p\hr.db")
print(con)
cur = con.cursor()
cur.execute("select * from employees")
for id, name, job, salary in cur.fetchall():
    print(f"{id:3} {name:30} {job:10} {salary:10}")

con.close()
