import math

a = float(input())
b = float(input())
c = float(input())

cos_a = (b**2 + c**2 - a**2) / (2 * b * c)
cos_b = (a**2 + c**2 - b**2) / (2 * a * c)
cos_c = (a**2 + b**2 - c**2) / (2 * a * b)

A = math.degrees(math.acos(cos_a))
B = math.degrees(math.acos(cos_b))
C = math.degrees(math.acos(cos_c))

print(A)
print(B)
print(C)