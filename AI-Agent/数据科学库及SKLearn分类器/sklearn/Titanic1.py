import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from scipy import sparse
from sklearn.linear_model import LogisticRegression

print(os.getcwd())

data = pd.read_csv(os.path.join('data', 'titanic_openml.csv'), na_values='?')
# print(data.head(7))
# print(data.tail(4))

y = data['survived']
X = data.drop(columns='survived')

# print(y)


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=12)

# clf = LogisticRegression()
# clf.fit(X_train, y_train)


ohe = make_pipeline(SimpleImputer(strategy='constant'), OneHotEncoder())
X_encoded = ohe.fit_transform(X_train[['sex', 'embarked']])
print(X_encoded.toarray())

col_cat = ['sex', 'embarked']
col_num = ['age', 'sibsp', 'parch', 'fare']

X_train_cat = X_train[col_cat]
X_test_cat = X_test[col_cat]
X_train_num = X_train[col_num]
X_test_num = X_test[col_num]

scaler_cat = make_pipeline(SimpleImputer(strategy='constant'), OneHotEncoder())
scaler_num = make_pipeline(SimpleImputer(strategy='mean'), StandardScaler())

X_train_cat_scaled = scaler_cat.fit_transform(X_train_cat)
X_test_cat_scaled = scaler_cat.transform(X_test_cat)
X_train_num_scaled = scaler_num.fit_transform(X_train_num)
X_test_num_scaled = scaler_num.transform(X_test_num)

X_train_scaled = sparse.hstack((X_train_cat_scaled,
                                sparse.csr_matrix(X_train_num_scaled)))
X_test_scaled = sparse.hstack((X_test_cat_scaled,
                               sparse.csr_matrix(X_test_num_scaled)))

clf = LogisticRegression()
clf.fit(X_train_scaled, y_train)
accuracy = clf.score(X_test_scaled, y_test)
print("Accuracy score of the {} is {:.2f}".format(clf.__class__.__name__, accuracy))

