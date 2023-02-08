a = int(input())
b = input()
n = len(b)
result = []
result.append(a * int(b))
for i in range(n):
    c = a * int(b[i])
    result.append(c)
for j in result[::-1]:
    print(j)