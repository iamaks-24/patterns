n=int(input("enter n value"))
originaln=n
n=2*n-1
for i in range(0,n):
    for j in range(0,n):
        k=originaln-min(i,j,n-i,n-j)
        print(k,end=" ")
    print(" ")

 