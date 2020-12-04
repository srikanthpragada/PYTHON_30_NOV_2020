# Accept month number and display number of days in the month

month = int(input("Enter month :"))

if month == 2:
    year = int(input("Enter year :"))
    if year % 4 == 0:
        print(29)
    else:
        print(28)
elif month in [4, 6, 9, 11]:
    print(30)
else:
    print(31)
