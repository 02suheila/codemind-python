n,m,r=map(int,input().split())
s=2*n*m*r*512
d=(s//1024)
t=str(d)
k="KB"
H=t+k
print(H)
