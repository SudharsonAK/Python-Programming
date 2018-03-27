def rotate(n,k,m):
	r=[]
	for i in range(n-k,n):
		r.append(m[i])
	for i in range(n-k):
		r.append(m[i])
	print(r)
def main():
	try:
		n=int(input())
		k=int(input())
		m=[]
		for i in range(n):
			m.append(int(input()))
		rotate(n,k,m)
	except:
		print('null')
main()

