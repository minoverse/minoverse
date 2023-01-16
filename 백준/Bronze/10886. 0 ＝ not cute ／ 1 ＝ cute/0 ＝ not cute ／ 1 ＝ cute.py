total = 0
T = int(input()) # 테스트 케이스 수
for t in range(1, T+1):
    numbers = list(map(int,(input().split())))
    for number in numbers:
        total += number
if total <= T // 2:

    print("Junhee is not cute!")
else:
    print("Junhee is cute!")