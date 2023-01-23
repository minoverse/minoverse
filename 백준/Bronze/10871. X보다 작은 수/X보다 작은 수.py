N, x = map(int,input().split())
a = list(map(int, input().split()))
lis = []
for i in range(N):
    if a[i] < x :
        lis.append(a[i])
print(*lis)