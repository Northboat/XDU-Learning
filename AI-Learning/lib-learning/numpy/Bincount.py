import numpy as np

arr = np.array([0,0,1,1,2,2])
weight = np.array([0.1,0.3,0.3,0.5,0.6,0.2])

print(np.bincount(arr, weights=weight))

x = [[1,3,3],
     [7,5,2]]
print(np.argmax(x,axis=0))

y = np.around([-1.2798,1.2798,2.357,9.67,13], decimals=1)
print(y)

x = np.array([[1, 0], [2, -2], [-2, 1]])
print(np.where(x>0, x, 0))