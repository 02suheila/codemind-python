s1=input().lower()
s2=input().lower()
c=[]
g=s1.split()
h=s2.split()

for i in h:
    if i in g:
        c.append(i)
        
print(*c)