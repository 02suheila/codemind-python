s1=input().lower()
s2=input().lower()
a=set(s1)
b=set(s2)
v=''
g=''
for i in a:
    if i ==' ':
        continue
    if i not in b:
        g+=i       
for i in b:
    if i==' ':
        continue
    if i not in a:
        g+=i
b=''.join(sorted(g))
print(len(b))

    