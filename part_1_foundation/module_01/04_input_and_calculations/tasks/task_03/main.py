# Считает, сколько полных коробок получится и сколько штук останется
items = int(input("Enter number of items: "))
box_size = int(input("Enter box size: "))

# ошибка тут. Применяли деление к строкам - по этому применил приведение к типу int. И после деления - привел результат к типу int
full_boxes = int(int(items) / int(box_size))
left = items % box_size

# добавил f к f-strings
print(f"Full boxes: {full_boxes}")
print(f"Items left: {left}")
