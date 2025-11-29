import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure(num=8, figsize=(9,5))
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

# ,=表示取出可迭代对象中的唯一元素（即作用于只含有一个元素的迭代器）
l1 ,= plt.plot(x, y1, color='blue', linestyle='--', linewidth=1.0)
l2 ,= plt.plot(x, y2, color='red')
plt.legend(handles=[l1, l2], loc='best', labels=['Straight', 'Curve'])
plt.show()


x = np.linspace(-3,3,50)
y = 0.1*x

plt.figure()
plt.ylim(-2,2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

