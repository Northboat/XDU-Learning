import numpy as np

A = np.arange(12).reshape(3,4)
print(A)

A1 = np.split(A, 2, axis=1)
for item in A1:
    print(item)

A2 = np.split(A, 3, axis=0)
for item in A2:
    print(item)

A3= np.array_split(A,3,axis=1)
for item in A3:
    print(item)