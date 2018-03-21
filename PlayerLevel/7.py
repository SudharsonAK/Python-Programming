import re

pat = r'^[s-zA-Z]+$'

a = input()

if bool(re.match(pat, a)):
    n = len(a)
    if n % 2 != 0:
        print("Invalid")
    else:
        for i in range(0, n, 2):
            print(a[i+1] + a[i], end = "")
else:
    print("Invalid")
    
