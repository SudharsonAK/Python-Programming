n=input("\nEnter the N number")
m=int(input("\nEnter the K number"))
c=list(str(n))
e=m
while e>0:
    e=e-1
    del(c[e])
print(''.join(c))
