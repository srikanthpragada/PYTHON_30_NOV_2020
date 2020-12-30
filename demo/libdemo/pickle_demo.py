import pickle


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __str__(self):
        return f"{self.x},{self.y},{self.radius}"


c = Circle(10, 20, 30)
print(pickle.dumps(c))
