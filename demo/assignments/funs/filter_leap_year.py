def isleapyear(y):
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0


years = [2000, 2010, 2020, 2019, 2100, 2004]

for y in filter(isleapyear, years):
    print(y)
