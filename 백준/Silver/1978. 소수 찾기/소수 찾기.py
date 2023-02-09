n = int(input())
a = list(map(int, input().split()))   #소수의정의: 나누어 떨어지는 수가 1과자기자신뿐일때
lis = []
for i in a:
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
       lis.append(i)
print(len(lis))
