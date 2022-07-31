n=int(input())
l=list(map(int,input().split()))

t=int(input())
h=[]
for i in range(len(l)):
    if l[i]==t:
        h.append(i)
if t not in l:
    print("-1")
else:
    print(*h)
