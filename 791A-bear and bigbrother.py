x,y = map(int, input().split())
n = 0
while x <= y:
        x = x * 3 
        y = y * 2
        n += 1
 
print(n)