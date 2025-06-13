import numpy as np

#create two dimentioanl vectors
A = np.array([[1, 2, 5], [3, 4, 6], [5, 6, 8]])

print(" Array dimentions:" , A.ndim)  # Number of dimensions
print(" Array shape:", A.shape)  # Shape of the array
# Broadcasting example
vector = np.array([1, 0, 0])
result = A + vector  # Adds vector to each row of the matrix
print("Result of broadcasting:\n", result)

print("Array data type:", A.dtype)  # Data type of the array elements
print("Array size:", A.size)  # Total number of elements in the array


#slicing example

A = np.array([[1, 2, 5], [3, 4, 6], [5, 6, 8]])

print( A[0,0:2] )  # Slicing the first row, first two elements

print( A[0:2, 1] )  # Slicing the first two rows, second column
print( A[0:2, 1:3] )  # Slicing the first two rows, second and third columns
print( A[0:2, 1:3] )  # Slicing the first two rows, second and third columns


# 2d Vector additions
A = np.array([[1, 2, 5], [3, 4, 6], [5, 6, 8]])
B = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])

print( A+B)
print( np.add(A, B) )  # Element-wise addition using numpy's add function

# 2d Vector subtraction
print( A-B)
print( np.subtract(A, B) )  # Element-wise subtraction using numpy's subtract function

# 2d Vector multiplication
print("multiply", A*B) # dot product of 1 row and 1 column of two matrix
print( "multiply : ",np.multiply(A, B) )  # Element-wise multiplication using numpy's multiply function

#dot product of 2d vectors
print("dot product", np.dot(A, B))  # Dot product of two 2D arrays
# Element-wise division
print("divide", A/B)
print("divide : ", np.divide(A, B))  # Element-wise division using numpy's divide function
# Transpose of a 2D array
print("Transpose of A:\n", A.T)  # Transpose of matrix A