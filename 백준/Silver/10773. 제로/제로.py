T = int(input()) # 테스트 케이스 수
a = []
for t in range(1, T+1):
    b = int(input())
    if b == 0:
        a.pop()
    else:
        a.append(b)
print(sum(a))
