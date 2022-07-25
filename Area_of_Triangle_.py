import math
A,B,C=map(int,input().split())
e=A+B+C
s=e/2
a=math.sqrt((s*(s-A)*(s-B)*(s-C)))
print("%0.2f"%a)