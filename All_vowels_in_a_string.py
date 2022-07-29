n=input()

f="aeiou"
l=[]
for i in f:
    if i in n:
        if i not in l:
            l.append(i)

if len(l)==5:
    print(True)
else:
    print(False)
