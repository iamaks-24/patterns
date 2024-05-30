n=int(input("enter n value:"))
for i in range(n,0,-1):
    spaces=n-i
    for j in range(1,i+1):
        print(" "*spaces+"*",end=" ")
        spaces=0
    print()
for i in range(1,n+1):
    spaces=n-i
    for j in range(1,i+1):
        print(" "*spaces+"*",end=" ")
        spaces=0
    print()