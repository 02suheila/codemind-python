s=input()
dic={}
for i in s:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
c=0
for k,v in dic.items():
    if v==1:
        c+=1


if len(s)==c:
    print(True)
else:
    print(False)
