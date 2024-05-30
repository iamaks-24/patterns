n=int(input("enter n value"))
total_cols=0
spaces=0
for i in range(1,2*n+1):
    if i>n:
        total_cols=2*n-i
    else:
        total_cols=i
    spaces=n-total_cols
    for j in range(1,total_cols+1):
        print(" "*spaces + "*",end=" ")
        spaces=0
    print(" ")

#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *