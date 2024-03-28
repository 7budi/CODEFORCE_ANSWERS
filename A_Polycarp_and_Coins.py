#first take the number of test cases
T = int(input())
n=[]
c2=[]
#Second take the test cases
for i in range(T):
    n.append(int(input()))

#Third make a loop to through all the test cases
for i in range(len(n)):
   #forth divide the T.C by 3 and assign it to c2
   c2.append(int(n[i] // 3))

c1 = list(c2)
#fifth maka aonther loop to sum c1 and c2 and  cheak if the total is equal to n
for j in range(len(n)):
    if c2[j]*2 + c1[j] != n[j]:
        if c2[j]*2 + c1[j] + 1 == n[j]:
            c1[j] +=1
        elif c2[j]*2 + c1[j] + 2 == n[j]:
            c2[j] +=1
for c1,c2 in zip(c1,c2):
    print(c1,c2)
   


#This is the simple version
#for s in[*open(0)][1:]:n=int(s);print(c:=n//3+n%3%2,n-c>>1)