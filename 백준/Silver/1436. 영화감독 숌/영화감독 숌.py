n = int(input())
i = 1
cnt = 0
while n != cnt:
    i += 1
    if '666' in str(i):
        cnt += 1
    if n == cnt:
        break
print(i)