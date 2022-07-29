n=input()
m=input()
f="AEIOUaeiou"
l=[]
for i in range(len(n)):
    if m==n[i]:
        print(True)
        print(i)
        break
else:
    print(False)

