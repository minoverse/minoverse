rest = []
double = [] #중복되는 요소 구별할 리스트
for _ in range(10):
 number = int(input())
 a = number % 42
 rest.append(a)
for i in rest:
    if i not in double:
        double.append(i)   #double의 len이 겹치는거 빠진 개수
print(len(double))