lisa = []
lisb = []
# T = int(input()) # 테스트 케이스 수
for t in range(1, 4):
 a, b = list(map(int,input().split()))
 lisa.append(a)
 lisb.append(b)
 
for i in lisa:
    if lisa.count(i) ==1:
        x = i
for j in lisb:
    if lisb.count(j) ==1:
        y = j
print(x, y)
