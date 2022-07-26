n=int(input())
l=list(map(int,input().split()))
e=[]
a=0
for i in range(len(l)):
    s=0
    k=l[i]
    while k>0:
        r=k%10
        s=s+r
        k=k//10
    e.append(s)
    a=a+e[i]
print(a)    