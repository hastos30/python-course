name = "Viktor"
age = 25

print(name)
print("Age:", age)

age = 26
print("Next years:", age)

greeting = "Hello, " + name
print(greeting)

print("--- Types ---")

count = 25
price = 19.99
title = "Book"
is_done = False
deadline = None

print(type(count))
print(type(price))
print(type(title))
print(type(is_done))
print(type(deadline))

age_text = "25"
print(type(age_text))

print("--- Conversion ---")

age_text = "25"
age = int(age_text)
print(age_text, type(age_text))
print(age, type(age))

print(age_text * 2)
print(age * 2)

price = float("19.99")
print(price, type(price))
print(int(price))

message = "Age: " + str(age)
print(message)

print("--- Tracing ---")

items = 3
price = "40"
total_text = price + "0"
total = int(total_text) * items
label = "Total: " + str(total)
print(label)

print("Total: " + str(total))

a = "3"
b = 2
c = a * b
d = int(c) + b
e = float(d) / 5
a = d
print(a, c, e)
print("a =", a, type(a))
print("c =", c, type(c))
print("e =", e, type(e))
