import numpy as np
import pandas as pd

from sklearn.datasets import load_boston
boston = load_boston()

boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
boston_df.head()

# What is the target? - price
boston_df['PRICE'] = boston.target

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

Y = boston_df['PRICE']
X = boston_df.drop(['PRICE'], axis=1, inplace=False)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# Build linear regression model
lr = LinearRegression()
lr.fit(X_train, Y_train)
Y_predict = lr.predict(X_test)

# Evaluate the performance of the model! R2
R2 = r2_score(Y_test, Y_predict)

# Print out the model and the performance
print(f'Y-intercept: {lr.intercept_}')
print(f'Coefficients: {np.round(lr.coef_, 2)}')