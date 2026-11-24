age = int(input("Age: "))
day = input("Day (Mon-Sun): ")

if age < 7:
    price = 0
elif age < 18:
    price = 5
elif age >= 65:
    price = 6
else:
    price = 10

if day in ("Sat", "Sun") and price > 0:
    price = price + 2

print(f"Ticket price: {price}")
