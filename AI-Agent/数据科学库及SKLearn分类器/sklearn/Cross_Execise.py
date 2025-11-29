from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_validate
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import SGDClassifier

pipe = make_pipeline(StandardScaler(), SGDClassifier(max_iter=1000))
scores = cross_validate(pipe, X, y,  scoring='balanced_accuracy',
                        cv=3, return_train_score=True)

import pandas as pd
import matplotlib.pyplot as plt

df_scores = pd.DataFrame(scores)
df_scores[['train_score', 'test_score']].boxplot()
plt.show()
print(df_scores)
