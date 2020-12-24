class Cricketer:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"{self.name} - {self.country}"


class Batsman(Cricketer):
    def __init__(self, name, country, runs):
        Cricketer.__init__(self, name, country)
        self.runs = runs

    def __str__(self):
        return super().__str__() + f" - {self.runs}"

    def points(self):
        return self.runs // 50


class Bowler(Cricketer):
    def __init__(self, name, country, wickets):
        Cricketer.__init__(self, name, country)
        self.wickets = wickets

    def __str__(self):
        return super().__str__() + f" - {self.wickets}"

    def points(self):
        return self.wickets // 2


class AllRounder(Batsman, Bowler):
    def __init__(self, name, country, runs, wickets):
        # Call __init__ of both super classes
        Batsman.__init__(self, name, country, runs)
        Bowler.__init__(self, name, country, wickets)

    def points(self):
        return Batsman.points(self) + Bowler.points(self)

    def __str__(self):
        return f"{self.name} - {self.country} - {self.runs} - {self.wickets}"


bat = Batsman("Dhoni", "India", 4500)
print(bat)
print(bat.points())

bow = Bowler("Marshall", "Westindies", 350)
print(bow)
print(bow.points())

ar = AllRounder("Hadle", "NZ", 3500, 250)
print(ar)
print(ar.points())
