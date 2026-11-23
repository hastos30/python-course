a = 17
b = 5

print("--- Arithmetic ---")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a**2)

print(10 / 2)
print(type(10 / 2))

print("--- Precedence ---")
print(2 + 3 * 4)
print((2 + 3) * 4)

print("--- Seconds ---")
total_seconds = int(input("Enter seconds: "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{total_seconds} s = {hours} h {minutes} min {seconds} s")
