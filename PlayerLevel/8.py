def camel(string):
	s=string.split(' ')
	a='' 
	for i in range(len(s)):
		s[i]=s[i].capitalize()
		a+=s[i]+' '
	print(a)
def main():
  try:
    string=input()
    camel(string)
  except:
    print('invalid')
main()
