T = int(input()) # 테스트 케이스 수
for t in range(1, T+1):
    a = int(input()) 
    q = a //25
    b = a - (25 *q)
    d = b // 10
    c = b - (10 * d)
    n = c // 5
    e = c - (5 * n)
    p = e // 1
    print(q, d, n, p)
