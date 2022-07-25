N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
d=[]
for i in A:
    for j in B:
        if i==j:
            if j not in d:
                d.append(j)
            if i not in d:
                d.append(i)
print(*d)                
            