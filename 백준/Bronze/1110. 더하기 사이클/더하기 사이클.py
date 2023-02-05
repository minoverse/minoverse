n = int(input())
first = n
cnt = 1
a = n // 10
b = n % 10
c = (a + b) % 10
n =(10 * b) + c
while n != first:
      a = n // 10
      b = n % 10
      c = (a + b) % 10
      n =(10 * b) + c
      cnt += 1
      if n == first:
        break
print(cnt)