T = int(input()) # 테스트 케이스 수
for t in range(1, T+1):
    a, b = list(map(int,input().split()))
    total = a + b
    print(f"Case #{t}: {a} + {b} = {total}")