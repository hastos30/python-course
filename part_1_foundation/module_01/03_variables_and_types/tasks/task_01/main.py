product_name = "Keyboard"
price = 300.50
quantity = 4
in_stock = True
discount = None

print("Product name:", product_name, type(product_name))
print("Price:", price, type(price))
print("Quantity:", quantity, type(quantity))
print("Stock:", in_stock, type(in_stock))
print("Discount:", discount, type(discount))

total = price * quantity

print("Total: " + str(total))
