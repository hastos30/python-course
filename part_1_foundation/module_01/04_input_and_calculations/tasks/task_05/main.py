items = int(input("Enter number of items: "))
box_size = int(input("Enter box size: "))

full_boxes = int(int(items) / int(box_size))
left = items % box_size

boxes_needed = (items + box_size - 1) // box_size

print(f"Full boxes: {full_boxes}")
print(f"Items left: {left}")
print(f"Boxes needed: {boxes_needed}")
