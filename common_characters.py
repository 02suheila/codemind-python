s1=input().lower()
s2=input().lower()
a=set(s1)
b=set(s2)
g=''

for i in a:
    if i ==' ':
        continue
    if i in b:
        if i not in g:
                g+=i       
for i in b:
    if i==' ':
        continue
    if i in a:
        if i not in g:
            g+=i
    
b=''.join(sorted(g))
if len(b)==0:
    print("-1")
else:
    print(b)




        