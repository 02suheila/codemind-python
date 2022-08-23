n=input()
l=[]
v=0
for i in n:
    if i.isdecimal():
        l.append(i)
        v+=int(i)
print(v)