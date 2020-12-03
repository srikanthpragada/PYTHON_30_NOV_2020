# Calculate amount

price = int(input("Enter price :"))
qty = int(input("Enter qty   :"))

if qty > 5:
    price = price * 0.80   # 20% discount
else:
    price = price * 0.90   # 10% discount

amount = price * qty

print(f"Amount = {amount:8.2f}")


