n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
r=[]
flag=0
for i in range(len(l)):
    if l[i]>=a and l[i]<=b:
        flag=1
        r.append(l[i])
        

if flag==0:
    print("-1")
else:
    print(min(r))