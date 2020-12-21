class Student:
    def __init__(self, name, fee):
        self.name = name
        # Private attribute
        self.__fee = fee


s = Student("Tom", 10000)
s.course = "Python"   # Create an object attribute
print(s.__dict__)
print(s.name, s._Student__fee)
