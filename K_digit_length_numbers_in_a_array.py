m,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    d=str(abs(i))
    
    if k==len(d):
        c+=1
print(c)