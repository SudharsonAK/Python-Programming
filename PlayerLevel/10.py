def timetomin(t0,t1):
	l1=t0.split(':')
	l2=t1.split(':')
	(tt0,tt1)=(int(l1[0]),int(l2[0]))
	(tm0,tm1)=(int(l1[1]),int(l2[1]))
	if tt0<tt1:
		return False
	time=tt0-tt1
	mins=tm0-tm1
	mins+=(time*60)
	print('Minutes :',mins)
def main():
	try:
		t0=input()
		t1=input()
		timetomin(t0,t1)
	except:
		print('invalid')
main()
