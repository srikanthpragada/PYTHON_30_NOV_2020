class Account:
    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # Object attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    # Methods
    def __str__(self):
        return f"{self.acno} {self.ahname} {self.balance}"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


a = Account(1, "Scott", 20000)  # Create an object
a.deposit(20000)
print(a)
a2 = Account(2, "Richards")
a2.deposit(10000)
print(a2.balance)
