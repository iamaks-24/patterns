n=int(input("enter n value"))
c=0
spaces=0
for i in range(1,2*n+1):
    if i>n:
        c=2*n-i
    else:
        c=i
    spaces=n-c
    for j in range(c,0,-1):
        print("  "*spaces + str(j) ,end=" ")
        spaces=0
    for k in range(2,c+1):
        print(k,end=" ")
    print()
#       1
#     2 1 2
#   3 2 1 2 3
# 4 3 2 1 2 3 4