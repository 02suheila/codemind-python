A,B=map(int,input().split())
N=list(map(int,input().split()))
M=list(map(int,input().split()))
d=[]

for i in N:
    for j in M:
        if i==j:
            if j not in d:
                d.append(j)
            if i not in d:
                d.append(i)

print(len(d))        
        
