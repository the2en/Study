import pandas as pd
import statsmodels.api as sm

# 1. read dataset
df = pd.read_csv("./data/Sample_data_titanic.csv", header = 0)

# 2. make dummies
df['Sex'] = df['Sex'].astype('category') ###categorization
df = pd.get_dummies((df))
print(df.dtypes)

# 3. data splitting
Y = df['Survival'] ### dependent variable
X = df.loc[:, ~df.columns.insin(['Survival'])]
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 0)

# 4. model fitting and prediction
X_train = sm.add_constant(X_train)
logit_model = sm.Logit(Y_train, X_train)
result = logit_model.fit_regularized(method='l1', alpha=0.1, maxiter=1000)
print(result.summary())

X_test = sm.add_constant(X_test)
Y_pred = result.predict(X_test)
Y_pred = [1 if x > 0.5 else 0 for x in Y_pred]

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

confusion_matrix(Y_test, Y_pred)
accuracy = accuracy_score(Y_test, Y_pred)
precision = precision_score(Y_test, Y_pred)
recall = recall_score(Y_test, Y_pred)

print('Acc: {0:.3f}, Precision: {0:.}, Recall: {0:.}', )

import matplotlib.pyplot as plt
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
# Plot the data points before clustering
axs[0].scatter(X[:, 0], X[:, 1])
