'''ML: Clustering
College of Global Business
Hoon Jang
[GLOB 347] Lecture note #9
Agenda
• What is Clustering?
• K-means Clustering Algorithm
• Demo & Practice
2
Acknowledgements
All of the lecture notes for this class borrowed with/without modification from the sources
including lecture notes (prof. Tibshirani, G’Sell, Shalizi, Chouldechova, Franklin, etc.) and
books (Introduction to Business Analytics by Jaggia et al, etc.)
WHAT IS CLUSTERING?
Recall the Unsupervised Learning…
• Unsupervised learning, also called Descriptive analytics,
describes a family of methods for uncovering latent
structure in data
• In unsupervised learning, we just look at data xi
– This is called “un-labelled” data
– Even if we have labels, we may still wish to temporarily ignore the
labels, and conduct unsupervised learning on the inputs xi
4
Clustering Has One or More Goals:
• Segmentation: Segment a large set of cases into small
subsets that can be treated similarly
• Compression: Generate a more compact description of a
dataset
• Representation: Model an underlying process that
generates the data as a mixture of different, localized
processes
5
Examples of Clustering Tasks
• Identify similar groups of online shoppers based on their
browsing and purchasing history
• Identify similar groups of music listeners or movie viewers based
on their ratings or recent listening/viewing patterns
• Cluster input variables based on their correlations to remove
redundant predictors from consideration
• Cluster hospital patients based on their medical histories
• Determine how to place sensors, broadcasting towers, law
enforcement, or emergency-care centers to guarantee that
desired coverage criteria are met
6
Example of Clustering
7
Raw data One possible way to cluster the data
Another Example of Clustering
• Here’s a less clear example. How should we partition it?
8
Does it make sense?
Terminology
• Hard clustering: items assigned to a unique cluster
• Soft clustering: cluster membership is a real-valued
function, distributed across several clusters
9
K-MEANS CLUSTERING ALGORITHM
K-means Clustering
• Main idea: A good clustering is one for which the withincluster variation is as small as possible
• The within-cluster variation for cluster Ck
:
– Some measure of the amount by which the observations within each
class differ from one another, we will denote it by WCV(Ck
)
• Goal: Find K clusters (C1
, C2
, …, Ck
) that minimize
– This says: Partition the observations into K clusters such that the
WCV summed up over all K clusters is as small as possible
11
෍
𝑘=1
𝐾
𝑊𝐶𝑉(𝐶𝑘)
K-means Clustering
• The standard K-means algorithm is based on Euclidean
distance
• The cluster quality measure is an intra-cluster measure only,
equivalent to the sum of item-to-centroid
• A simple greedy algorithm locally optimizes an intra-cluster
measure – the sum of item-to-centroid
– Find the closest cluster center for each item and assign it to that
cluster
– Recompute the cluster centroid as the mean of items, for the newlyassigned items in the cluster
12
How to Define Within-Cluster Variation?
• Recall that the goal is to find K clusters which minimize
σ𝑘=1
𝐾 𝑊𝐶𝑉(𝐶𝑘)
• Typically, if we use Euclidean distance, then:
• To be clear: we’re treating K as fixed ahead of time
– We are not optimizing K as part of this objective!!!
13
• Assume that n = 5, K = 2, and the full distance matrix for all 5
observations is shown below:
• Possible clustering results would be shown in Red or Blue
• It’s easy to see that the Blue clustering minimizes the within-cluster
variation among all possible partitions of the data into K = 2 clusters
Simple Example of K-means Clustering
14
K-means Clustering Algorithm
• Cluster centers: Can pick by sampling the input data
15
K-means Clustering Algorithm
• Assign points to closest center
16
K-means Clustering Algorithm
• Recompute centers (Old = cross, New = dot)
17
K-means Clustering Algorithm
• Iterate:
– 1) For fixed number of iterations
– 2) Until no change in assignments or small change in quality
18
Summary of K-means
• We’d love to minimize
• It’s infeasible to actually optimize this in practice, but K-means at least
gives us a so-called local optimum of this objective
• The result we get depends both on K, and also on the random
initialization that we wind up with
– It’s a good idea to try different random starts and pick the best results among them
• There’s a method called K-means++ that improves how the clusters are
initialized
19
DEMO & PRACTICE
Practice Problem
• Some facts of using ML in a marketing domain:
– More than 97% of marketers believe that to be successful in digital
marketing, machine learning tools will play a crucial role
– 40% of US companies use ML to improve sales and marketing
– More than 76% of US companies exceeded their sales targets with
the help of machine learning
– European banks increased sales by 10% and reduced churn rate by
20%
21
https://channels.theinnovationenterprise.com/articles/3-ways-digitalmarketers-can-use-machine-learning
Netflix?
• Saved $1 billion after implementing machine learning
algorithm which recommends highly personalized TV
programs to their subscribers!
22
Data
• Objective: Group customers by using the data!
• Transactional data set which contains all the transactions occurring between
01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail
– The company mainly sells unique all-occasion gifts
• Attribute data
– Invoice No.: Invoice number. Nominal, a 6-digit integral number uniquely assigned to each
transaction. If this code starts with letter 'c', it indicates a cancellation
– Stock code: Product (item) code. Nominal, a 5-digit integral number uniquely assigned to each
distinct product
– Description: Product (item) name. Nominal
– Quantity: The quantities of each product (item) per transaction. Numeric
– Invoice Date: Invoice Date and time. Numeric, the day and time when each transaction was
generated
– Unit Price: Unit price. Numeric, Product price per unit in sterling
– Customer ID: Customer number. Nominal, a 5-digit integral number uniquely assigned to each
customer
– Country: Country name. Nominal, the name of the country where each customer resides.
23
Demo
• The goal: group customers into three clusters
– Use only features colored in red (See the prior slide)
• Let’s see what happens if you change the # of clusters
(from three to six)
24'''