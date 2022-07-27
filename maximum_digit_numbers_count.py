n=int(input())
l=list(map(int,input().split()))
d=[]
for i in l:
    s=str(abs(i))
    g=len(s)
    #print(g)
    d.append(g)
for i in l:
    s=str(abs(i))
    g=len(s)

    if max(d)==g:
        print(i,end=" ")
