import numpy as np
a = np.array([1,2,3], dtype=np.int32)
print(a)
print(type(a))
print(a.dtype)

b = np.array([[2,3,4],[3,4,5]])
print(b)


c = np.zeros((3,4))
print(c)


d = np.ones((3,4), dtype=np.int32)
print(d)

e = np.empty((3,4))
print(e)

f = np.arange(10, 21, 2)
print(f)

g = f.reshape((2,3))
print(g)

h = np.linspace(0,11,12)
print(h)

i = h.reshape((3,4))
print(i)