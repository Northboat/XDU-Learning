import os
import pandas as pd


data = pd.read_csv(os.path.join('data', 'adult_openml.csv'), na_values='?')
# print(data.head(7))

y = data['class']
X = data.drop(columns=['class', 'fnlwgt', 'capitalgain', 'capitalloss'])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=12)
# print(y_train)

col_cat = ['workclass', 'education', 'marital-status', 'relationship', 'race', 'sex', 'native-country']
col_num = ['age', 'education-num', 'hoursperweek']

X_train_cat = X_train[col_cat]
X_test_cat = X_test[col_cat]
X_train_num = X_train[col_num]
X_test_num = X_test[col_num]

from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline


cat_pipe = make_pipeline(SimpleImputer(strategy='constant'), OneHotEncoder())
num_pipe = make_pipeline(SimpleImputer(strategy='mean'), StandardScaler())

X_train_cat_scaled = cat_pipe.fit_transform(X_train_cat)
X_test_cat_scaled = cat_pipe.transform(X_test_cat)
X_train_num_scaled = num_pipe.fit_transform(X_train_num)
X_test_num_scaled = num_pipe.transform(X_test_num)

import numpy as np
from scipy import sparse

X_train_scaled = sparse.hstack((X_train_cat_scaled, 
                sparse.csr_matrix(X_train_num_scaled)))
X_test_scaled = sparse.hstack((X_test_cat_scaled, 
                sparse.csr_matrix(X_test_num_scaled)))

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train_scaled, y_train)
accuracy = clf.score(X_test_scaled, y_test)
print('accuracy of the {} is {:.2f}'.format(clf.__class__.__name__, accuracy))