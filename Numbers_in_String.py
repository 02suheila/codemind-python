n=input()
v=0
for i in n:
    if i.isdecimal():
        v+=int(i)
print(v)