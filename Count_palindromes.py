n=int(input())
l=list(map(int,input().split()))
e=[]
c=0
for i in range(len(l)):
    s=0
    k=l[i]
    while k>0:
        r=k%10
        s=s*10+r
        k=k//10
    e.append(s)
    if l[i]==e[i]:
        c+=1
print(c)        
