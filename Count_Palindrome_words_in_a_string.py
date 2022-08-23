s=input().lower()

x=s.split()

c=0
for i in x:
    f=i[::-1]

    

    if f==i:
        c+=1
print(c)
