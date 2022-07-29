n=input()
r=n.split()
y="AEIOUaeiou"
h=[]
for i in r:
    c=len(i)
    d=0
##    print(c)
    for j in range(c):
        if i[j] in y:
            d+=1
    h.append(d)
print(*h)    