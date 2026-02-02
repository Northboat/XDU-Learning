from sklearn.datasets import load_breast_cancer
from sklearn.metrics import balanced_accuracy_score

X, y = load_breast_cancer(return_X_y=True)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=12, stratify=y)

from sklearn.pipeline import make_pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler

pipe = make_pipeline(StandardScaler(), SGDClassifier(max_iter=1000))

from sklearn.model_selection import GridSearchCV

param = {'sgdclassifier__loss': ['hinge', 'log'],
         'sgdclassifier__penalty': ['l2','l1']}
grid = GridSearchCV(pipe, cv=3, n_jobs=1, param_grid=param, return_train_score=True)
grid.fit(X_train, y_train)

accuracy = grid.score(X_test, y_test)


from sklearn.model_selection import cross_validate
import pandas as pd
import matplotlib.pyplot as plt

scores = cross_validate(grid, X, y, scoring='balanced_accuracy',
                        cv=3, return_train_score=True)
df_scores = pd.DataFrame(scores)
df_scores[['train_score', 'test_score']].boxplot()
plt.show()

print(grid.best_params_)
print(df_scores)
print(accuracy)

