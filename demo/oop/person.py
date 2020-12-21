class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


# p = Person("Scott", 30)   # p.__init__()
# p2 = Person("Scott", 30)
# print(p)  # str(p) ->  p.__str__()
# print(p == p2)  # p1.__eq__(p2)

persons = [Person("A", 10), Person("B", 30), Person("C", 20)]

for p in sorted(persons):
    print(p)

print(persons[0] > persons[1])
