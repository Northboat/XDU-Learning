import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2
# 设置图片名称figure3，大小为(8,5)
# 要先设置画布，才能plot(布局)
plt.figure(num=5, figsize=(8, 5))
# 设置曲线颜色、宽度、线段类型（虚线，默认实线）
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.plot(x, y2)
# 展示图片
plt.show()

plt.figure(num=6, figsize=(8,5))
plt.plot(x, y2)
plt.plot(x, y1, color='blue', linewidth=1.5, linestyle='--')

plt.xlim(-1,2)
plt.ylim(-2,3)

plt.xlabel('price')
plt.ylabel('earn')

x_ticks = np.linspace(-1,2,5)
print(x_ticks)
plt.yticks(np.linspace(-2,3,5),
           ['very bad','bad','so so','good','very good'])
plt.xticks(x_ticks)
plt.show()

