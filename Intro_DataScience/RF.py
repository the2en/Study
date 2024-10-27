import numpy as np
import pandas as pd

from sklearn.datasets import load_breast_cancer
b_cancer = load_breast_cancer()

b_cancer_df = pd.DataFrame(b_cancer.data, columns=b_cancer.feature_names)
b_cancer_df['diagnosis'] = b_cancer.target
print(f'Datasets: {b_cancer_df.shape}')
print(f'Data info: {b_cancer_df.info()}')

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
b_cancer_scaled = scaler.fit_transform(b_cancer.data)

from sklearn.model_selection import train_test_split

Y = b_cancer_df['diagnosis']
X = b_cancer_scaled
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, Y_train)
Y_predict = rf.predict(X_test)

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

# Results (DT)
# Acc: 0.918
# Precision: 0.961, Recall:0.907, F1:0.933
# ROC_AUC: 0.922

# Results (LR)
# Acc: 0.977
# Precision: 0.973, Recall:0.991, F1:0.982
# ROC_AUC: 0.972

# Results (DT)
# Acc: 0.953
# Precision: 0.972, Recall:0.954, F1:0.963
# ROC_AUC: 0.953

from sklearn.model_selection import GridSearchCV

params = {'max_depth': [2, 4, 6, 8, 10]}

grid_cv = GridSearchCV(rf, param_grid=params, scoring = 'accuracy', cv=5, return_train_score=True)
grid_cv.fit(X_train, Y_train)

cv_result_df = pd.DataFrame(grid_cv.cv_results_)
cv_result_df[['param_max_depth', 'mean_test_score', 'mean_train_score']]

print('Maximum accuracy: {0:.3f}, (Sub)optimal hyper-parameter: {1}'.format(grid_cv.best_score_, grid_cv.best_params_))

# 1st-trial
# Acc: 0.953
# Precision: 0.972, Recall:0.954, F1:0.963
# ROC_AUC: 0.953