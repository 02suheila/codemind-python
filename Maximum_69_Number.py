n=int(input())
d=str(n)
l=list(d)
for i in range(len(l)):
    if l[i]=='6':
        l[i]='9'
        break
s=''.join(l)    
print(int(s))