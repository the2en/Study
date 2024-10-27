import pandas as pd
from statsmodels.tools import add_constant
import statsmodels.api as sm

# 1. read dataset
df = pd.read_csv("./data/Midterm.csv", header=0)
print(df.dtypes)

## 2. make dummies
df['IS_WEEKEND'] = df['IS_WEEKEND'].astype('category')
df['IS_LOWSEASON'] = df['IS_LOWSEASON'].astype('category')  ###categorization
df = pd.get_dummies((df))
print(df.dtypes)

## 3. data splitting
Y = df['SALES']
X = df.iloc[:, df.columns != 'SALES']
X = add_constant(X)

## 4. perform linear regression with statsmodels to get p-values for each independent variable
model = sm.OLS(Y, X).fit()
print(model.summary())
#