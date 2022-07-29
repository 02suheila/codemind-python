n=input()
l=n.split()
d=[]
s='AEIOUaeiou'
for i in l:
    c=0
    for j in i:
        if j in s:
            c+=1
    d.append(c)
e=[]
for i in d:
    if i == min(d):
         e.append(i)
print(len(e))          
         