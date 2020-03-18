def find_min(a, b, c, d):
    return min(a, min(b, min( c, d)))
a=[]
for i in range (0,4):
    a.append(int(input()))

print(find_min(a[0],a[1],a[2],a[3]))