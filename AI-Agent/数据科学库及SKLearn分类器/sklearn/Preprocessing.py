from sklearn.datasets import load_boston
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=12)


from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression

# clf = LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=1000, random_state=42)
# clf.fit(X_train, y_train)
# accuracy = clf.score(X_test, y_test)
# print('Accuracy score of the {} is {:.2f}'.format(clf.__class__.__name__, accuracy))
# print('{} required {} iterations to be fitted'.format(clf.__class__.__name__, clf.n_iter_[0]))


scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)



clf = LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=1000, random_state=42)
clf.fit(X_train_scaled, y_train)
accuracy = clf.score(X_test_scaled, y_test)
print('Accuracy score of the {} is {:.2f}'.format(clf.__class__.__name__, accuracy))
print('{} required {} iterations to be fitted'.format(clf.__class__.__name__, clf.n_iter_[0]))

# 错误的预处理方式，直接对为拆分的数据集进行标准化，即`X_scaled = fit_transform(X)`
# 再对`X_scaled`进行独立拆分

# 这里的`fit_transform`方法只使用一次，其作用为拟合并标准化
# 若多次使用，每次拟合的效果不同，将对标准化的结果造成较大误差