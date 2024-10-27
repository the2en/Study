import pandas as pd
from sklearn.cluster import KMeans

# Load the dataset
df = pd.read_csv('./data/kMeans_Test.csv')
X = df[['MntPurchases', 'NumofPurchases']].values

# Perform k-means clustering
kmeans = KMeans(n_clusters=6)
kmeans.fit(X)

# Get the cluster labels and cluster centers
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Plot the data points and cluster centers after clustering
# Create subplots for the figures
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Plot the data points before clustering
axs[0].scatter(X[:, 0], X[:, 1])
axs[0].set_title('Data Pints before Clustering')
axs[0].set_xlabel('MntPurchases')
axs[0].set_ylabel('NumofPurchases')
axs[1].scatter(X[:, 0], X[:, 1], c=labels)
axs[1].scatter(centers[:, 0], centers[:, 1], marker='*', s=200, c='red')
axs[1].set_title('K-means Clustering')
axs[1].set_xlabel('MntPurchases')
axs[1].set_ylabel('NumofPurchases')

# Adjust spacing between subplots
plt.tight_layout()

# Display both figures
plt.show()