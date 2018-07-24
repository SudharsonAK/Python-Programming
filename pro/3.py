def findrepn(li):
	li.sort()
	rep=[]
	a=len(li)
	for i in range(1,a):
			if li[i]==li[i-1] :
				if li[i] in rep :
					continue
				rep.append(li[i])
	print(rep)

def main():
	try:
		li=[]
		a=int(input())
		for i in range(a):
			li.append(int(input()))
		findrepn(li)
	except:
		print('Unique')

main()
