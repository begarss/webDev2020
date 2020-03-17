from math import sqrt

a = int(input())
b = int(input())
for x in range(a,b+1):
    if(x%sqrt(x)==0):
        print(x)