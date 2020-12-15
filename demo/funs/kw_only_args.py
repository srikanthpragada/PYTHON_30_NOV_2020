# Keyword-only arguments
def area(*, length, width):
    return length * width


print(area(width=10, length=20))
print(area(length=10, width=50))
