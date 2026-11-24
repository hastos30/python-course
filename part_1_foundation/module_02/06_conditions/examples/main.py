name = input("Name: ")
age = int(input("Age: "))
has_ticket = input("Ticket? (yes/no): ") == "yes"

if not name:
    print("Error: name is empty")
elif age >= 18 and has_ticket:
    print(f"Welcome, {name}!")
elif age < 18 or not has_ticket:
    print(f"Sorry, {name}, entry denied")

if 0 <= age <= 120:
    print("Age looks valid")

print(bool(""), bool("0"), bool(0), bool(None))
