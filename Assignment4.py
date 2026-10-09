import numpy as np
# Matrix Addition using List
a = [[1, 2],[3, 4]]
b= [[5, 6],[7, 8]]

result_list = [[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        result_list[i][j] = a[i][j] + b[i][j]

print("Matrix A:")
for row in a:
    print(row)

print("\nMatrix B:")
for row in b:
    print(row)

print("\nSum (List Addition):")
for row in result_list:
    print(row)

print("=================================================================")

# Matrix Addtion using Numpy
np_a = np.array([[1, 2],[3, 4]])
np_b = np.array([[5, 6],[7, 8]])

print("\nNumPy Array A:\n", np_a)
print("\nNumPy Array B:\n", np_b)
print("\nSum (NumPy Addition):\n", np_a+np_b)
