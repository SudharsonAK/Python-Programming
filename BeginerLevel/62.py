a=raw_input()

flag=0
for b in a:
	
if((b == '0') or (b == '1')):
		
flag+=1
if(flag==(len(a))):
	
print("yes")

else:
	
print("no")