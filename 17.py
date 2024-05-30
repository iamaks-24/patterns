n=int(input("enter n value: "))
spaces,c=0,0
for i in range(1,2*n+1):
    if i>n:
        c=2*n-i
    else:
        c=i
    spaces=n-c
    for k in range(c,0,-1):
        print(" "*spaces+str(k),end="")
        spaces=0
    for j in range(2,c+1):
        print(j,end="")
    print()
#    1
#   212
#  32123
# 4321234
#  32123
#   212
#    1