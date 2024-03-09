s = input()
U = 0
L = 0
for i in s:
    if i.isupper():
        U += 1
    else:
        L += 1
if U < L or U == L:
    print(s.lower())
else:
    print(s.upper())
        