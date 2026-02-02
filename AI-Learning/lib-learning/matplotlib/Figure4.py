import numpy as np
import matplotlib.pyplot as plt

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

plt.plot(x, y, lw=10, zorder=1)
# 对被遮挡的图像调节相关透明度，本例中设置 x轴 和 y轴 的刻度数字进行透明度设置
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    '''
    其中label.set_fontsize(12)重新调节字体大小 bbox设置目的内容的透明度相关参
    facecolor调节 box 前景色 edgecolor 设置边框， 本处设置边框为无 alpha设置透明度.
    '''
    # 其中label.set_fontsize(12)重新调节字体大小，bbox设置目的内容的透明度相关参，
#     facecolor调节 box 前景色，edgecolor 设置边框， 本处设置边框为无，alpha设置透明度.
    label.set_bbox(dict(facecolor='white',edgecolor='none',alpha=0.7))

plt.show()
