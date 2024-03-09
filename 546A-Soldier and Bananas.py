k,n,w = map(int , input().split())
z = 0
for i in range(w + 1):
    z += k * i 
if z > n:
    print(z - n)
else:
    print("0")