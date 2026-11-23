bill = float(input("Enter bill: "))
tip_percent = int(input("Enter tip percent: "))
people = int(input("Enter people: "))

tip = bill * (tip_percent / 100)
total = bill + tip
price_per_person = total / people

print(f"Tip: {tip:.2f}")
print(f"Total: {total:.2f}")
print(f"Per person: {price_per_person:.2f}")

# Ошибка. ZeroDivisionError line 7 деление на ноль
