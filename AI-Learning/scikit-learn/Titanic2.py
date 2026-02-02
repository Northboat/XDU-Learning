from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import os
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(os.path.join('data','titanic_openml.csv'), na_values='?')
y = data['survived']
X = data.drop(columns='survived')

# print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=12)

# print(y_train)

col_cat = ['sex', 'embarked']
col_num = ['age', 'sibsp', 'parch', 'fare']

pre_cat = make_pipeline(SimpleImputer(strategy='constant'), OneHotEncoder(handle_unknown='ignore'))
pre_num = make_pipeline(SimpleImputer(strategy='mean'), StandardScaler())

preprocessor = make_column_transformer((pre_cat, col_cat), (pre_num, col_num))
pipe = make_pipeline(preprocessor, LogisticRegression(solver='lbfgs'))
pipe.fit(X_train, y_train)
accuracy = pipe.score(X_test, y_test)
print('Accuracy score of the {} is {:.2f}'.format(pipe.__class__.__name__, accuracy))

param = {'columntransformer__pipeline-2__simpleimputer__strategy': ['mean', 'median'],
        'logisticregression__C': [0.1, 1.0, 10]}
grid = GridSearchCV(pipe, param_grid=param, cv=5, n_jobs=1)
grid.fit(X_train, y_train)
print('Accuracy score of the {} is {:.2f}'.format(grid.__class__.__name__, grid.score(X_test, y_test)))

scores = cross_validate(grid, X, y, scoring='balanced_accuracy', cv=5, n_jobs=-1, return_train_score=True)
df_scores = pd.DataFrame(scores)
df_scores[['train_score', 'test_score']].boxplot()
plt.show()

#%%
