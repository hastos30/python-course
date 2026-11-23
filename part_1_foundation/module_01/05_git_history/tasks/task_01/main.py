input_minutes = int(input("Enter a number in minutes: "))

hours = input_minutes // 60
minutes = input_minutes % 60

print(f"{input_minutes} minutes = {hours} hours {minutes} minutes")
