a=raw_input()
for c in range (0,a):
if (any(c.isalpha for c in a) and any(c.isdigit for c in a)):
    print("YES")
else:
    print("NO")
