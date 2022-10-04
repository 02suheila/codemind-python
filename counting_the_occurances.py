a=input()
b=input()
d={}
c=[]
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for k,v in d.items():
    if k==b:
        c.append(v)
if len(c)==0:
    print("-1")
else:
    print(*c)