a = int(input())
b = int(input())
c = int(input())
n = a + b + c
if n == 180 and a == b == c:
 print("Equilateral")
elif n ==180 and a == b:
 print("Isosceles")
elif n ==180 and b == c:
 print("Isosceles")
elif n ==180 and c == a:
 print("Isosceles")
elif n == 180:
 print("Scalene")

else:
 print("Error")