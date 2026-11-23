year = "2026"
birth_year = 1999

# TypeError: unsupported operand type(s) for -: 'str' and 'int'. нужно привести yers к int
age = int(year) - birth_year

# TypeError: can only concatenate str (not "int") to str. age нужно привести к str - что бы склеить
print("Age: " + str(age))

# ValueError: invalid literal for int() with base 10: '1.80'. вместо int использовть функцию float
height = float("1.80")
print("Height:", height)
