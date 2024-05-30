n=int(input("enter n value"))
spaces=0
for i in range(n,0,-1):
    if i==n:
        print("*"* (2*n-1))
        continue
    spaces=n-i
    for j in range(i,0,-1):
        if j==i:
            print(" "*spaces + "*" ,end="")
            spaces=0
        else:
            print(" ",end="")
    for k in range(2,i+1):
        if k==i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
# *********
#  *     *
#   *   *
#    * *
#     *