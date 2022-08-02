n=int(input())
l=list(map(int,input().split()))
s=0
r=0
for i in range(n):
    if i%2==0:
        s+=l[i]
        
    if i%2!=0:
        r+=l[i]
k=s-r        

if k==0:
    print('YES')
else:
    print('NO')
        
