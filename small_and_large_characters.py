s1=input().lower()

d=s1.split()
for i in d:
    print(min(i),max(i),end=" ")