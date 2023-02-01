x, y = map(int, input().split())
n = int(input())
ny = y + n
nx = x
while ny > 59:
    ny = ny - 60
    nx += 1
    if ny <= 59:
        break
while nx > 23:
    nx = nx - 24
    if nx <= 23:
        break
print(nx, ny)