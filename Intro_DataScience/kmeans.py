import numpy as np
import pandas as pd
import math

retail_df = pd.read_excel('./data/Online_Retail_Final.xlsx')
print(retail_df.head())

# Data Cleansing steps
retail_df = retail_df[retail_df['Quantity'] > 0]
retail_df = retail_df[retail_df['UnitPrice'] > 0]
retail_df = retail_df[retail_df['CustomerID'].notnull()]

# Remove duplicates if exists
retail_df.drop_duplicates(inplace=True)

# CustomerID's data type from float to int
retail_df['CustomerID'] = retail_df['CustomerID'].astype(int)

# We have to construct features
# Salesamount = Quan * UnitPrice
# Order Freg

retail_df['SalesAmount'] = retail_df['UnitPrice'] * retail_df['Quantity']
print(retail_df.head())

aggregations = {
    'InvoiceNo':'count',
    'SalesAmount':'sum'
}

# Create feauture set
customer_df = retail_df.groupby('CustomerID').agg(aggregations)
customer_df = customer_df.reset_index()
customer_df = customer_df.rename(columns={'InvoiceNo':'Freq'})

print(customer_df.head())

import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
ax.boxplot([customer_df['Freq'], customer_df['SaleAmount']], sym='bo')
plt.xticks([1, 2], ['Freq', 'SaleAmount'])
plt.show()

# re-scale data points
customer_df['Freq_log'] = np.log1p(customer_df['Freq'])
customer_df['SalesAmount_log'] = np.log1p(customer_df['SalesAmount'])

fig, ax = plt.subplots()
ax.boxplot([customer_df['Freq_log'], customer_df['SalesAmount_log']], sym='bo')
plt.xticks([1, 2], ['Freq_log', 'SalesAmount_log'])
plt.show()

# Let's do K-means
from sklearn.cluster import KMeans

X_features = customer_df[['Freq_log', 'SalesAmount_log']].values

# Not that required
from sklearn.preprocessing import StandardScaler
X_features_scaled = StandardScaler().fit_transform(X_features)

kmeans = KMeans(n_clusters=3, random_state=0)
Y_labels = kmeans.fit_predict(X_features_scaled)

customer_df['ClusteringResults'] = Y_labels
print(customer_df.head())