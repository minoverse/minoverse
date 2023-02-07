n = int(input())
lis = []
grade = []

for i in range(1, n + 1):
    line = list(map(int, input().split()))
    lis.append(line)
for i in range(n): 
    cnt = 1                                                                                                        #for문에서 i,j로 따로 놓고 range(n)까지 해서 비교
    for j in range(n): 
        if lis[i][0] < lis[j][0] and lis[i][1] < lis[j][1] :
           cnt += 1
    grade.append(cnt)
           
print(*grade)
              
