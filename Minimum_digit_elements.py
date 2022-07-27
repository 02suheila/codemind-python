n=int(input())
l=list(map(int,input().split()))
c=0
d=[]
for i in l:
    j=str(i)
    h=len(j)
    
    d.append(h)
for i in l:
    j=str(i)
    h=len(j)    
    if min(d)==h:
        c+=1
print(c)        