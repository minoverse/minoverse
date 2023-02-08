lis = [1, 1, 2, 2, 2, 8]
a = list(map(int, input().split()))
result = []
for i in range(len(a)):
    result.append(lis[i] - a[i])
print(*result)