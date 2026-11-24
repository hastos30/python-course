a = float(input())
b = float(input())
c = float(input())

if a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b:
    print("Not a triangle")
elif a == b == c:
    print("equilateral")
elif a == b or b == c or a == c:
    print("isosceles")
else:
    print("scalene")
