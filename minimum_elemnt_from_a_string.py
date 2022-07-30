n=input()
k=n.split()
l=list(k)
p=k[-1]
g=min(p)
#print(g)
flag=0
for i in p:
    if g.lower()==i:
        d=i
        flag=1
if flag==0:
    print(g)
    
else:
    print(d)