n=int(input())
k=[]
a=0
b=1
if n==0:
    print(True)
elif n==1 or n==2:
    print(True)
else:
    for i in range(n):
        c=a+b
        a=b
        b=c
        k.append(c)
if n in k:
    print(True)
else:
    print(False)