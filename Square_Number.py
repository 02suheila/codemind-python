n=int(input())
l=n
for i in range(0,n+1):
    d=i*i
    if d==l:
        print(True)
        break
else:
    print(False)