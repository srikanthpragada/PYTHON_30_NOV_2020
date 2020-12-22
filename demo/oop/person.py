class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0 and value <= 120:
            self.__age = value

    def __str__(self):
        return f"{self.name} - {self.__age}"

    def __eq__(self, other):
        return self.name == other.name and self.__age == other.__age

    def __lt__(self, other):
        return self.__age < other.__age

    @property
    def type(self):
        if self.__age < 30:
            return "Young"
        elif self.__age < 60:
            return "Middle Aged"
        else:
            return "Old"


p = Person("Scott", 20)  # p.__init__()
p.age = 140   # Assign value to property
print(p.age)
print(p.type)  # Property
# p2 = Person("Scott", 30)
# print(p)  # str(p) ->  p.__str__()
# print(p == p2)  # p1.__eq__(p2)

# persons = [Person("A", 10), Person("B", 30), Person("C", 20)]
#
# for p in sorted(persons):
#     print(p)
#
# print(persons[0] > persons[1])
