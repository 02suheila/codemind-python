n=input().lower()
vin="aeiou"
v=0
c=0
s=0
g=[]
f=" "
for i in n:
    if i in vin:
        v+=1
    elif i.isdecimal():
        g.append(i)
    elif i not in vin and i not in f:
        c+=1
    else:
        s+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",len(g))
print("White spaces:",s)

