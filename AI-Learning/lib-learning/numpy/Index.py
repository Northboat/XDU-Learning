import numpy as np

B = np.array([1,2,3])
print(B[0]==1) # True
print(B[2]==3) # True

B = np.arange(1,13).reshape((3,4))
print(B[0]) # [1,2,3,4]
print(B[0][0]) # 1

for row in B: # 一行一行打印
    print(row)
for colume in B.T: # 一列一列打印
    print(colume)

print(B[1,1:3]) # [6,7]

C = B.flatten()
D = list(B.flat)
print(C)
print(D)