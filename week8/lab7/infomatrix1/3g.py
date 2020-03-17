from math import sqrt

a = int(input())
check=False
for x in range(2,int(sqrt(a)+1)):
    if(a%x==0):
        print(x)
        check=True;

if check==False:
    print(a)