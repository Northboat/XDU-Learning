import numpy as np
import pylab as pl
from scipy import spatial

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']

# np.random.rand将随机生成[0,1)的浮点数，接收参数整型为生成浮点数个数
x = np.sort(np.random.rand(100))
# print(x)
# 用np.searchsorted(迭代器, 数)寻找最近旁点下标（取上限）
idx = np.searchsorted(x,0.5)
print(x[idx], x[idx-1])




np.random.seed(42)
N = 100
# 生成(-1,1)的随机数共一百行，每行两列
points = np.random.uniform(-1,1,(N,2))
kd = spatial.cKDTree(points)
# 要寻找旁点的点
targets = np.array([[0, 0], [0.5, 0.5],
                    [-0.5, 0.5], [0.5, -0.5],
                    [-0.5, -0.5]])
print(targets)
dist, idx = kd.query(targets, 3)
print(dist)
print(idx)
print(points[83])

r = 0.2
idx2 = kd.query_ball_point(targets, r)
print(idx2)

idx3 = kd.query_pairs(0.1)-kd.query_pairs(0.08)
print(idx3)