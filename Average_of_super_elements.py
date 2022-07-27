n=int(input())
l=list(map(int,input().split()))
d=[]
for i in l:
    c=l.count(i)
    #print(i,c)
    if c==i:
        if c not in d:
            d.append(c)
f=sum(d)

if len(d)==0:
    print("-1")
else:
    a=f/len(d)
    print("%0.2f"%a)