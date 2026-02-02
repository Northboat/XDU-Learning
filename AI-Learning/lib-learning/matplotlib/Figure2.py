import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

x0 = 1
y0 = 2*x0+1

# 设置坐标轴
plt.figure(num=8, figsize=(9,5))
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
# 绘制散点图，若为单个点，即为描点
plt.scatter(x0,y0, s=70, color='b')
plt.plot(x, y1)
plt.plot([x0,x0],[0,y0], ls='--',lw=2.5, c='black')
plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
plt.text(-3,3,'wdnmd',fontdict={'size':'16', 'color':'black'})
plt.show()