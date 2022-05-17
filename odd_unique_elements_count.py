n=int(input())
l=list(map(int,input().split()))
r=[]

c=0
for i in l:
    if i not in r:
        r.append(i)
#print(r)        
for j in r:
    if j%2:
        c+=1
print(c)        