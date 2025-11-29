from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler

pipe = make_pipeline(MinMaxScaler(),
                     LogisticRegression(solver='saga', multi_class='auto',
                                        random_state=12, max_iter=5000))

print(pipe.get_params())

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=12)

# 使用网格搜索找到当前训练集下最优参数
from sklearn.model_selection import GridSearchCV
import pandas as pd

param = {'logisticregression__C': [0.1, 1.0, 10],
         'logisticregression__penalty': ['l2', 'l1']}
grid = GridSearchCV(pipe, param_grid=param, cv=3, n_jobs=1, return_train_score=True)
grid.fit(X_train, y_train)
print(grid.get_params())

df_grid = pd.DataFrame(grid.cv_results_)
print(df_grid)

print(grid.best_params_)

accuracy = grid.score(X_test, y_test)
print('Accuracy score of the {} is {:.2f}'.format(grid.__class__.__name__, accuracy))



from sklearn.model_selection import cross_validate
import matplotlib.pyplot as plt

scores = cross_validate(grid, X, y, cv=3, n_jobs=1, return_train_score=True)
df_scores = pd.DataFrame(scores)
print(df_scores)
df_scores[['train_score', 'test_score']].boxplot()
plt.show()
