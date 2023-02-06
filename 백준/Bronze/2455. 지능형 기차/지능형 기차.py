result = []
out_ = []
in_ = []
total = 0
for i in range(1,5):
    a, b = map(int, input().split())
    total = total + (-a) + b
    result.append(total)
print(max(result))