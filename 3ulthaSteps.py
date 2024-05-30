# n=int(input("enter n value"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("* ",end=" ")
#     print(" ")

# try to find formula relating row n column

n=int(input("enter n value"))
for i in range(1,n+1):
    for j in range(1,(n-i+1)+1):
        print("* ",end=" ")
    print(" ")

# *****
# ****
# ***
# **
# *