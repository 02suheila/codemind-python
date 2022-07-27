n=int(input())
l=list(map(int,input().split()))
d=[]
for i in l:
    c=l.count(i)
    if c==i:
        if c not in d:
            d.append(c)
if len(d)==0:
    print("-1")
else:    
    print(*d)        