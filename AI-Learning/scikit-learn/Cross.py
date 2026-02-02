from sklearn.datasets import load_digits
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

X, y = load_digits(return_X_y=True)
pipe = make_pipeline(MinMaxScaler(),
                    LogisticRegression(max_iter=1000, solver='lbfgs', multi_class='auto', random_state=12))


from sklearn.model_selection import cross_validate
scores = cross_validate(pipe, X, y, cv=3, return_train_score=True)

import pandas as pd
import matplotlib.pyplot as plt

df_scores = pd.DataFrame(scores)
df_scores[['train_score', 'test_score']].boxplot()
plt.show()
print(df_scores)
