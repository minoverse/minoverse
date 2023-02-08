h, m = map(int, input().split())
if m < 45 and h > 0:
   nh = h -1
   nm = m + 15
   
elif m < 45 and h == 0:
    nm = m + 15
    nh = 23
elif m >= 45:
    nh = h
    nm = m - 45
else: pass
print(nh, nm)