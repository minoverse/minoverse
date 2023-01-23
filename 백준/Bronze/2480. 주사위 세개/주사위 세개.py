a = list(map(int, input().split()))
b = sorted(a)
if b[0] == b[2]:
    print(b[0] * 1000 + 10000)
elif b[0] == b[1] and b[1] < b[2]:
    print(b[1] * 100 + 1000)
elif b[1] == b[2] and b[0] < b[1]:
    print(b[1] * 100 + 1000)
else:
    print(b[2] * 100)
