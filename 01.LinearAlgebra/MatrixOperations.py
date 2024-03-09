import numpy as np

# Define the matrices
A = np.array([[1, 1], [-1, 1]])
B = np.array([[1, 5, 2], [2, 4, 2]])

print("Matrix A:\n", A)
print("\n")
print("Matrix B:\n", B)
print("\n")

# Perform matrix multiplication
RES1 = np.dot(A, B)

# Print the outcomes and parameter count
print("Matrix A * Matrix B:\n", RES1)
print("\n")

# Define the matrices
A = np.array([[1, 1], [-1, 1]])
B = np.array([[1, 5], [2, 4]])

print("Matrix A:\n", A)
print("\n")
print("Matrix B:\n", B)
print("\n")

RES2 = np.concatenate((A, B))

print("Matrix A concatenate Matrix B:\n", RES2)
print("\n")

# Define the matrices
A = np.array([[1, 1], [-1, 1]])
B = np.array([[1, 5], [4, 2]])

print("Matrix A:\n", A)
print("\n")
print("Matrix B:\n", B)
print("\n")

RES3 = np.add(A,B)

print("Matrix A + Matrix B:\n", RES3)
print("\n")
