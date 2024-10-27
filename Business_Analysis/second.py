#### Week 13 - Problem 01 ####
######### 이름: 김세은 #########

import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('framingham.csv')
print(df.dtypes)

df.dropna()

formula = "TenYearCHD~male+age+currentSmoker+cigsPerDay+BPMeds+prevalentStroke+prevalentHyp+diabetes+totChol+sysBP+diaBP+BMI+heartRate+glucose"
model = smf.logit(formula, data=df)
result = model.fit()

print(result.summary())

fig, ax = plt.subplots(ncols=3, nrows=2, figsize=(20,20))
sns.countplot(x='male', hue='TenYearCHD', data=df, ax=ax[0,0])
sns.scatterplot(x='TenYearCHD', y='age', hue='TenYearCHD', data=df, ax=ax[0,1])
sns.boxplot(x='TenYearCHD', y='cigsPerDay', data=df, ax=ax[0,2])
sns.boxplot(x='TenYearCHD', y='totChol', data=df, ax=ax[1,0])
sns.boxplot(x='TenYearCHD', y='sysBP', data=df, ax=ax[1,1])
sns.boxplot(x='TenYearCHD', y='glucose', data=df, ax=ax[1,2])
plt.show()