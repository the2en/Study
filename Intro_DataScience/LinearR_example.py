import numpy as np
import pandas as pd
from statsmodels.tools import add_constant
import statsmodels.api as sm

## 1. read dataset
df = pd.read_csv("./data/sample_data.csv", header = 0)
print(df.dtypes)

## 2. check for missing data and drop rows with missing data
missing_prop = df.isnull().mean().max()
if missing_prop > 0.1:
    df.fillna(df.mean(), inplace=True)
else:
    df.dropna(inplace=True)

## 3. make dummies
#df['Sex'] = df['Sex'].astype('category')
#df['Pclass'] = df['Pclass'].astype('category') ###categorization
#df['Embarked'] = df['Embarked'].astype('category')
#df['Survival'] = df['Survival'].astype('category')
#df = pd.get_dummies((df))
#print(df.dtypes)

## 4. data scaling # optional
#from sklearn.preprocessing import StandardScaler
#scaler = StandardScaler()
#df_scaled = scaler.fit_transform(df)


## 5. data splitting
from sklearn.model_selection import train_test_split
Y = df['MonthlyCharge']
X = df.iloc[:,df.columns != 'MonthlyCharge'] ## iloc[row_index, column_index] iloc[:,:] -> select all rows/cols iloc[[1,4,7],:] -> select 2nd, 5th, 8th rows
X = add_constant(X)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 1234)

print(X_test)

## 6. perform linear regression with statsmodels to get p-values for each independent variable
model = sm.OLS(Y_train, X_train).fit()
print(model.summary())

## 7. make predictions on the test set
#Y_pred = model.predict(X_test)

## 8. evaluate the model performance on the test set
#from sklearn.metrics import mean_squared_error, r2_score
#mse = mean_squared_error(Y_test, Y_pred)
#r2 = r2_score(Y_test, Y_pred)
#print("Mean squared error: ", mse)
#print("R2 score: ", r2)
