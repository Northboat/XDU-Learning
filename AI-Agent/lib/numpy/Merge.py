import numpy as np

A = np.array([4,5,6])
B = np.array([1,2,3])
print(A)
print(B)

C = np.vstack((A,B))
print(C)

D = np.hstack((A,B))
print(D)

print(A.shape)
A1 = A[np.newaxis, :]
A2 = A[:, np.newaxis]
print("A1: ", A1)
print("A2:\n",A2)

B1 = B[np.newaxis, :]
B2 = B[:, np.newaxis]
print("B1: ", B1)
print("B2:\n", B2)


E1 = np.hstack((A1,B1))
E2 = np.vstack((A1,B1))
print(E1)
print(E2)
E3 = np.hstack((A2,B2))
print(E3)
