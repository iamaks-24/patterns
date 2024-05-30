# # analyzing formula
# ->consider having 2n rows
# if row_no>n:
#     col=n-(row-n+1) ,within bracket is the evacuating space 
#      col=2n-row+1
# else:
#    col=rowff

n=int(input("enter n value"))
c=0
for i in range(1,2*n+1):
    if i>n:
        c=2*n-i
    else:
        c=i
    for j in range(1,c+1):
        print("* ",end=" ")
    print(" ")
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *