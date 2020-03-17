import math

a = int(input())
check=False
cnt=0
for x in range(1,int(math.sqrt(a))):
    if(a%x==0):
        cnt+=1
if a%int(math.sqrt(a)) == 0:
    print(cnt*2+1)
else:
    print(cnt*2)
