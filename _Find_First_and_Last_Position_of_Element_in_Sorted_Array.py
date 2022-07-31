n=int(input())
l=list(map(int,input().split()))

t=int(input())
l.sort()
h=[]
for i in range(len(l)):
    if l[i]==t:
        h.append(i)
for j in h:        
    u=h[0]
    r=h[-1]
if t not in l:
    print("-1 -1")
else:
    print(u,r) 