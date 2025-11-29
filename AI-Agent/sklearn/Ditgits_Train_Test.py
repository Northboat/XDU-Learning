from sklearn.datasets import load_digits
# 关于手写数字识别的数据集
import matplotlib.pyplot as plt

# X的每行是64个图像像素的强度
# y是每个图片识别出来的数字0-9
X, y = load_digits(return_X_y=True)
print("X:{0}\n{1}".format(len(X), X))
print("y:{0}\n{1}".format(len(y), y))

# 绘制一下图片，灰度图
plt.imshow(X[0].reshape(8,8), cmap='gray')
plt.axis('off') # 关闭坐标轴
plt.show()
print("\nthe digit in the image is: ", y[0])

# 手动分割数据集
# 用多个独立的数据集训练模型
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=12)
print(X_test)

# 一旦拥有独立的训练和测试集，就可以使用fit方法学习机器学习模型
# 用score方法测试此方法
from sklearn.linear_model import LogisticRegression # 选择线性回归模型
# 建立线性回归模型
clf1 = LogisticRegression(solver='lbfgs',
                         multi_class='ovr', max_iter=5000, random_state=12)
# 通过已有数据集进行学习
clf1.fit(X_train, y_train)
accuracy1 = clf1.score(X_test, y_test)
print('Accuracy score of the {} is {:.2f}'.format(clf1.__class__.__name__, accuracy1))

# 同样我们还可以使用RandomForest模型进行学习，api基本保持一致
from sklearn.ensemble import RandomForestClassifier
# 建立模型
clf2 = RandomForestClassifier(n_estimators=100, n_jobs=-1,
                              random_state=12)
clf2.fit(X_train, y_train)
accuracy2 = clf2.score(X_test, y_test)
print('Accuracy score of the {} is {:.2f}'.format(clf2.__class__.__name__, accuracy2))




