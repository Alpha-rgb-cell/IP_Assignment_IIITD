n = int(input("Enter the number of row: "))
for i in range (n):
    for j in range (i+1):
        print("*",end=" ")
    for j in range (2*(n-i-1)):
        print(" ",end=" ")
    for j in range (i+1):
        print("*",end=" ")

    print()