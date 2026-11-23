number = int(input("Enter a 3-digit number: "))

hundreds = number // 100
tens = number % 100 // 10
units = number % 10

print(f"{hundreds} + {tens} + {units} = {hundreds + tens + units}")
