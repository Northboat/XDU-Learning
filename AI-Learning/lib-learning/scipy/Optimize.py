import matplotlib.pyplot as plt
import numpy as np

from math import sin,cos
from scipy import optimize

def f(x):
    x0,x1,x2 = x.tolist()
    return [5*x1+3, 4*x0**2-2*sin(x1*x2), x1*x2-1.5]

result = optimize.fsolve(f, [1,1,1])
print(result)
print(f(result))

def g(x):
    return [[0, 5, 0],
           [8*x[0], -2*cos(x[1]*x[2]), -2*x[1]*cos(x[1]*x[2])],
           [0, x[2], x[1]]]
result1 = optimize.fsolve(f, [1,1,1], fprime=g)
print(result1)



X = np.array([ 8.19,  2.72,  6.39,  8.71,  4.7 ,  2.66,  3.78])
Y = np.array([ 7.07,  2.78,  6.47,  6.71,  4.1 ,  4.23,  4.05])

def residuals(p):
    "计算以p为参数的直线和原始数据之间的误差"
    k, b = p
    return Y - (k*X + b)

# leastsq使得residuals()的输出数组的平方和最小，参数的初始值为[1,0]
r = optimize.leastsq(residuals, [1, 0])
k, b = r[0]
print(r)
print ("k =",k, "b =",b)
