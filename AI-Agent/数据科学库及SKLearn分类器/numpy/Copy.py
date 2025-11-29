import numpy as np

A = np.arange(4)
print(A)
B = A
C = A
D = A
A[0] = 11
print(A)
print(B)
print(C)

E = A.copy()
A[1] = 7
print(A)
print(E)
