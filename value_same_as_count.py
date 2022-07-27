n=int(input())
l=list(map(int,input().split()))
d=[]
for i in l:
    c=l.count(i)
    if c==i:
        if c not in d:
            d.append(i)
print(len(d))