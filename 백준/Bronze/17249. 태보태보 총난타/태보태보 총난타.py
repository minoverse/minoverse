a = list(input())
leftcnt = 0
cnt = 0

for j in a:
    if j =="@":
        cnt += 1
        
for i in range(len(a)):
    if a[i] == "(":
      n = int(i)
      
for i in a[0: n + 1]:
    if i == "@":
        leftcnt +=1

rightcnt = cnt -leftcnt

print(leftcnt, rightcnt)
