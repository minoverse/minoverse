T = int(input()) # 테스트 케이스 수
for t in range(1, T+1):
 N = int(input()) # 입력 줄 수
 a = list(map(int,input().split()))
 total = 0
 for elem in a:
  total += elem
 
 print(total)