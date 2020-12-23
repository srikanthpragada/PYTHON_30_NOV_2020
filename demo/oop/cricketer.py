class Cricketer:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name} - {self.country}"


class Batsman(Cricketer):
    def __init__(self, name, country, runs):
        super().__init__(name, country)
        self.runs = runs

    def __str__(self):
        return super().__str__() + f" - {self.runs}"

    def points(self):
        return self.runs // 50


class Bowler(Cricketer):
    def __init__(self, name, country, wickets):
        super().__init__(name, country)
        self.wickets = wickets

    def __str__(self):
        return super().__str__() + f" - {self.wickets}"

    def points(self):
        return self.wickets // 2


bat = Batsman("Dhoni", "India", 4500)
print(bat)
print(bat.points())

bow = Bowler("Marshall", "Westindies", 350)
print(bow)
print(bow.points())