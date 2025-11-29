import os
import pandas as pd

data = pd.read_csv(os.path.join('data', 'adult_openml.csv'), na_values='?')
# print(data.head(3))
y = data['class']
X = data.drop(columns=['class', 'fnlwgt', 'capitalgain', 'capitalloss'])
# print(X)

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=12)
# print(y_train)
encoder = LabelEncoder()
y_train = encoder.fit_transform(y_train)
y_test = encoder.transform(y_test)

from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

pre_cat = make_pipeline(SimpleImputer(strategy='constant'), OneHotEncoder(handle_unknown='ignore'))
pre_num = make_pipeline(SimpleImputer(strategy='mean'), StandardScaler())

col_cat = ['workclass', 'education', 'marital-status', 'relationship', 'race', 'sex', 'native-country']
col_num = ['age', 'education-num', 'hoursperweek']

preprocessor = make_column_transformer((pre_cat, col_cat), (pre_num, col_num))
# preprocessor.fit(X_train, y_train)

pipe = make_pipeline(preprocessor, LogisticRegression(solver='lbfgs', max_iter=5000))
# pipe.fit(X_train, y_train)

param = {'logisticregression__C': [0.1, 1.0, 10]}
grid = GridSearchCV(pipe, param_grid=param, cv=5, n_jobs=1)
grid.fit(X_train, y_train)
accuracy = grid.score(X_test, y_test)
print('accuracy of the {} is {:.2f}'.format(grid.__class__.__name__, accuracy))

from sklearn.model_selection import cross_validate
import matplotlib.pyplot as plt
scores = pd.DataFrame(cross_validate(grid, X, y, scoring='balanced_accuracy', cv=3, n_jobs=-1, return_train_score=True))
print(scores)
scores[['train_score', 'test_score']].boxplot(whis=10)
plt.show()