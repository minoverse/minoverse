n, m = map(int, input().split())
lis = list(map(int, input().split()))
maxtotal = 0
for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j+1, n):
            total = lis[i] + lis[j] + lis[k]
            if maxtotal <= total <= m:
               maxtotal = total
print(maxtotal)