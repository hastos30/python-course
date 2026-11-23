# Чек покупки: считаем сумму и печатаем её тремя способами
product = "Coffee"
price = 4.5
quantity = 3

total = price * quantity  # float * int даёт float

print("Total:", total)
print("Total: " + str(total))
print(f"Total: {total}")

print(f"{product} x {quantity} = {total}")
print(f"{product} x {quantity} = {price * quantity}")

# Деньги показываем с двумя знаками после точки
print(f"Price: {price:.2f}")
print(f"Third: {10 / 3}")
print(f"Third: {10 / 3:.2f}")

print("Total: {total}")
