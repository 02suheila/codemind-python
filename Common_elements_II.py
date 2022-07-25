A,B=map(int,input().split())
N=list(map(int,input().split()))
M=list(map(int,input().split()))
d=[]

for i in N:
    if i not in M:
        if i not in d:
            d.append(i)
for j in M:
    if j not in N:
        if j not in d:
            d.append(j)
print(*d)            
