import numpy as np
a = np.array([5,6,7,8])
b = np.arange(4)
print(a,b)

print(b*a, a.dot(b))

c = b**2
print(c)

d = np.sin(a)
e = np.cos(b)
print(d, e)

f = b*3
print(f)

g = b+3
print(g)

i = b>2
print(i)

j = a==b
print(j)

k = np.array([[1,1],[0,1]])
l = np.arange(4).reshape((2,2))
print(k)
print(l)

print(k.dot(l))
print(l.dot(k))
print(np.dot(k,l))
print(np.dot(l,k))

m = np.random.random((2,4))
print(m)
s = np.sum(m)

m2 = np.max(m)
m1 = np.min(m)
print("sum: ", s)
print("max: ", m2)
print("min: ", m1)

print("row sum: ", np.sum(m, axis=1))
print("colume min: ", np.min(m, axis=0))
print("row max: ", np.max(m, axis=1))

A = np.arange(2,14).reshape((3,4))
print(A)

# 最小元素索引
print(np.argmin(A))
# 最大元素索引
print(np.argmax(A))

print(np.mean(A))
print(np.average(A))
print(A.mean())

print(np.median(A))

print(np.sort(A))

print(np.transpose(A))
print(A.T)

print(np.clip(A,5,9))

