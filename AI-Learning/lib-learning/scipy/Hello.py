import numpy as np
import scipy
import matplotlib.pyplot as plt

print(scipy.__version__)


from scipy import constants as C

# 真空光速
print(C.c)
# 普朗克常数
print(C.h)
# pyysical_constants是一个常量字典，物理常量名为键，对应一个三元组，分别为常数值、单位和误差
print(C.physical_constants["electron mass"])

# 1英里等于多少米, 1英寸等于多少米, 1克等于多少千克, 1磅等于多少千克
print(C.mile)
print(C.inch)
print(C.gram)
print(C.pound)

import scipy.special as S

print (1 + 1e-20)
print (np.log(1+1e-20))
print (S.log1p(1e-20))

m = np.linspace(0.1, 0.9, 4)
u = np.linspace(-10, 10, 200)
results = S.ellipj(u[:, None], m[None, :])

print([y.shape for y in results])



m = np.linspace(0.1, 0.9, 4)
u = np.linspace(-10, 10, 200)
results = S.ellipj(u[:, None], m[None, :])
#%figonly=使用广播计算得到的`ellipj()`返回值
fig, axes = plt.subplots(2, 2, figsize=(12, 4))
labels = ["$sn$", "$cn$", "$dn$", "$\phi$"]
for ax, y, label in zip(axes.ravel(), results, labels):
    ax.plot(u, y)
    ax.set_ylabel(label)
    ax.margins(0, 0.1)
    
axes[1, 1].legend(["$m={:g}$".format(m_) for m_ in m], loc="best", ncol=2);
plt.show()
