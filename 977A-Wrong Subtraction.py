x, y = map(int, input().split())
for i in range(y):
   x = x // 10 if x % 10 == 0 else x - 1
print(int(x))
        