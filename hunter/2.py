n=[]
m=[]
a=int(input())
for i in range(0,a):
    m.append(int(input()))
    print(m)


m.sort(reverse=True)
print(m)
for i in m:
    n.append(str(i))
b=int("".join(n))
print (b)
