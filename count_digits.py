n=int(input())
l=list(map(int,input().split()))

for i in l:
    d=str(abs(i))
    print(len(d),end=" ")
