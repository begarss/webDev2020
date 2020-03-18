a = int(input())
b = []
sum = 0
for i in range(a):
    b.append(int(input()))
for i in range(a - 1):
    if(b[i] * b[i + 1] > 0):
        print("YES")
        exit(0)
print("NO")