n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if int(i**0.5)**2==i:
        c+=i
                    
        
print(c)        
        