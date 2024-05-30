n=int(input("enter n value"))
spaces=0
for i in range(1,2*n+1):
    if i>n:
        c=2*n-i
    else:
        c=i
    spaces=n-c
    for j in range(c,0,-1):
        if j==c:
            print(" "*spaces + "*" ,end="")
            spaces=0
        else:
            print(" ",end="")
    for k in range(2,c+1):
        if k==c:
            print("*",end="")
        else:
            print(" ",end="")
    print()
#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *