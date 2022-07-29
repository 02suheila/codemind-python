n=input().lower()
s="aeiou"
g=list(s)

l=[]
for i in s:
    if i not in n:
        if i not in l:
            l.append(i)
            
if len(l)==0:
    print("0")
else:
    print(*l)