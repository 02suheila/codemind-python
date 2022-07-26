N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
d=[]
c=0
for i in A:
   if i not in B:
       if i not in d:
           d.append(i)
           c+=1
for j in B:
    if j not in A:
        if j not in d:
            d.append(j)
            c+=1
print(c)

