n=int(input())
l=list(map(int,input().split()))
d=[]
for i in range(0,n,2):#12 32 52 72
    
    for j in range(l[i+1]):
        d.append(l[i])
print(*d)      