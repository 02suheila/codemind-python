n=int(input())
l=list(map(int,input().split()))
k=int(input())
d=[]
for i in l:
    c=l.count(i)
    if c==k:
        if i not in d:
            d.append(i)
if len(d)==0:
    print("-1")
else:    
    print(*d)
