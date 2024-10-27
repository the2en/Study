import numpy as np
import pandas as pd

from sklearn.datasets import load_breast_cancer
b_cancer = load_breast_cancer()

b_cancer_df = pd.DataFrame(b_cancer.data, columns=b_cancer.feature_names)
b_cancer_df['diagnosis'] = b_cancer.target

# Scaling our Dataset
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
b_cancer_scaled = scaler.fit_transform(b_cancer.data)

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Split our Dataset into training and testing
Y = b_cancer_df['diagnosis']
X = b_cancer_scaled
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# Build Decision Tree
dt = DecisionTreeClassifier(random_state=156)
dt.fit(X_train, Y_train)
Y_predict = dt.predict(X_test)

# Evaluate the model
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

confusion_matrix(Y_test, Y_predict)
acc = accuracy_score(Y_test, Y_predict)
pre_score = precision_score(Y_test, Y_predict)
rec_score = recall_score(Y_test, Y_predict)
f1_scoreX = f1_score(Y_test, Y_predict)
roc_auc = roc_auc_score(Y_test, Y_predict)

print('Acc: {0:.3f}'.format(acc))
print('Precision: {0:.3f}, Recall:{1:.3f}, F1:{2:.3f}'.format(pre_score, rec_score, f1_scoreX))
print('ROC_AUC: {0:.3f}'.format(roc_auc))

print(f'Y-ibtercept: {dt.intercept_}')
print(f'Coefficients: {np.round(dt.coef_, 2)}')

# Results (DT)
# Acc: 0.918
# Precision: 0.961, Recall:0.907, F1:0.933
# ROC_AUC: 0.922

# Results (LR)
# Acc: 0.977
# Precision: 0.973, Recall:0.991, F1:0.982
# ROC_AUC: 0.972