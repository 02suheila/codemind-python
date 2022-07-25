n,k=map(int,input().split())
l=list(map(int,input().split()))
d=[]
c=0
for i in range(len(l)):
    if l[i]%k==0:
        continue
    else:
        c+=1
print(c)
