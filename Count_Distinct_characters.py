n=input().lower()
s=''

for i in n:
    if i==' ':
        continue
    else:
        if i not in s:
            s+=i
            
    
f=''.join(sorted(s))
print(len(f))