n=input().lower()


dic={}

s=''
for i in n:
    if i==' ':
        continue
    else:
        if i not in dic:
        
            dic[i]=1
        else:
            dic[i]+=1
        
for k,v in dic.items():
    if v==1:
        s+=k
f=''.join(sorted(s))
print(f)