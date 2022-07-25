a=int(input())
n=list(map(int,input().split()))
flag=0
i=1
while i<len(n):
    if(n[i]<=n[i-1]):
        flag=1
    i+=1
    
if(flag==0):
    print("yes")
else:
    print("no")