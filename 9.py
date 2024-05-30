n=int(input("enter n value"))
spaces=0
for i in range(n,0,-1):
    spaces=n-i
    for j in range(i,0,-1):
        print(" "*spaces + "*" ,end="")
        spaces=0
    for k in range(2,i+1):
        print("*",end="")
    print()
#    *******
#     *****
#      ***
#       *