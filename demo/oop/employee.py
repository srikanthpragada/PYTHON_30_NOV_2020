class Employee:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

    def __str__(self):
        return f"{self.name} - {self.job} - {self.salary}"

    def __eq__(self, other):
        return self.name == other.name and self.job == other.job and self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    @property
    def netsalary(self):
        if self.job == "Programmer":
            return self.salary * 1.4
        else:
            return self.salary * 1.35


e1 = Employee("Mike", "DBA", 100000)
print(e1)
print(e1.netsalary)

employees = [Employee("Terry", "TL", 200000), Employee("Stevens", "Programmer", 70000),
             Employee("Tim", "DBA", 120000)]

for e in sorted(employees, reverse=True):
    print(e)
