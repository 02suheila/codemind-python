n=int(input())
l=list(map(int,input().split()))
s=0
r=[]
for i in l:
    if i not in r:
        r.append(i)
#print(r)        
        

for j in r:
    if j%2:
        s+=j
print(s)        
