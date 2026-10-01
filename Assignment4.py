rows = int(input("Enter number of rows = "))
columns = int(input("Enter number of columns = "))
a = []
n = 2
while (n>0):
    print ("Enter elements for the matrix ",n," = ")
    for i in range (columns):
        row = []
        print ("Row ",i+1)
        for j in range (rows):
            row.append(int(input()))
        a.append(row)
    
    print("The matrix as follows : ")
    for i in range (0,rows):
        for j in range (0,columns):
            print (a[i][j], end=" ")
        print()
