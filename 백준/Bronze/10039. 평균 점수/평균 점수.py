n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
result = [n1, n2, n3, n4, n5]
cnt = 0
total = 0
for element in result:
 if element >= 40:
    total += element
    cnt += 1
 else: 
    total += 40
    cnt += 1
print(int(total / cnt))
