n=int(input())
l=list(map(int,input().split()))
d=[]
for i in range(0,len(l),2):
    for j in range(l[i+1]):
        d.append(l[i])
print(*d)        