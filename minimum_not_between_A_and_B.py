n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
r=[]
flag=0
for i in range(len(l)):
    if l[i]>=a and l[i]<=b:
        continue
    else:
        r.append(l[i])
        flag=1
if(flag==1):
    print(min(r))
else:
    print("-1")
        