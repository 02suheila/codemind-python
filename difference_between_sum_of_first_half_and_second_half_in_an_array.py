n=int(input())
l=list(map(int,input().split()))
c=0
d=0
t=n//2
for i in range(len(l)):
    if i<t:
        c+=l[i]
    else:
        d+=l[i]
a=abs(c-d)
print(a)