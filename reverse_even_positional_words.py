n=input()
h=n.split()
l=[]
for i in range(len(h)):
    if i%2==0:
        h[i]=h[i][::-1]

print(*h)
