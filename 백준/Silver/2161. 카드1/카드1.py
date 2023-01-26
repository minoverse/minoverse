n = int(input())
a =list(range(1, n + 1))
d = []
while len(a) > 1:
    d.append(a.pop(0))
    a.append(a.pop(0))
print(*d, *a)