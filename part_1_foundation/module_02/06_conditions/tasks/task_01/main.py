number = int(input("Enter number: "))

negative_zero_positive = ""
even_odd = ""

if number < 0:
    negative_zero_positive = "negative"
elif number == 0:
    negative_zero_positive = "zero"
else:
    negative_zero_positive = "positive"

if number % 2 == 0:
    even_odd = "even"
else:
    even_odd = "odd"

print(f"{negative_zero_positive}, {even_odd}")
