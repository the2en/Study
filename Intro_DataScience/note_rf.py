'''ML: Classification (Random Forest)
College of Global Business
Hoon Jang
[GLOB 347] Lecture note #8
Agenda
• What is Random Forest
• Demo & Practice
2
Acknowledgements
All of the lecture notes for this class borrowed with/without modification from the sources
including lecture notes (prof. Tibshirani, G’Sell, Shalizi, Chouldechova, Franklin, etc.) and
books (Introduction to Business Analytics by Jaggia et al, etc.)
WHAT IS RANDOM FOREST?
Limitations of Decision Trees
• Decision trees are highly interpretable and fast to train
– Using greedy algorithm is a good choice!
• However, in order to capture a complex decision boundary,
we need to use a large tree (since each time we can only
make axis aligned splits!!)
– Large trees → High variance and are prone to overfitting
• In practice, decision tree models often underperform when
compared with other ML algorithms
4
Remedy for the Limitations
• One way to adjust for the high variance of the output is to
perform the experiment multiple times and then average the
results
– For a classification problem, we return the class that is outputted
by the plurality of the models
• It is called as “Bagging”, short for, of course, Bootstrap
aggregating (Breiman, 1996)
5
Bagging
• Bagging enjoys the benefits of…
– High expressiveness: By using full trees, each model is able to
approximate complex functions and decision boundaries
– Low variance: Averaging the prediction of all the models reduces
the variance in the final prediction, assuming that we choose a
sufficiently large number of trees
6
Improving on Bagging
• In practice, the ensembles of trees in Bagging tend to be
highly correlated
– All the original features are considered at every split of every tree
– E.g., Suppose we have an extremely strong predictor, xj
, in the
training set amongst moderate predictors. Then, the greedy
algorithm ensures that most of the models in the ensemble will
choose to split on xj
in early iterations
7
→ Each tree in the ensemble is identically distributed, with the expected
output of the averaged model the same as the expected output of any one
of the trees
Improving on Bagging
• Though six decision trees with different bootstrapped
samples are built, we can see a similar structure
→ Known as Tree correlation
8
Random Forest
• A modified form of bagging that creates ensembles of
independent decision trees
– Help to reduce tree correlation by injecting more randomness into
the tree-growing process
• To de-correlate the trees, we:
– Train each tree on a separate bootstrap sample of the full training
set
– For each tree, at each split, we randomly select a subset of the full
set of predictors
– Typical default values are p
1/2(where p is the # of total features,
classification), but this should be considered a tuning parameter
9
(Appendix) Out-of-the-box Performance
• RFs have become popular
– They tend to provide very good out-of-the-box performance
• From Probst, Bischle, and Boulesteix (2018),
– RFs have the least variability in their prediction accuracy
– RFs show better OOB errors than many other ML models
10
Tuning Random Forest
• RFs have multiple hyper-parameters to tune:
– The number of trees in the forest
– The number of features to consider at any given split
– The complexity of each tree
– The sampling scheme
– The splitting rule to use during tree construction
– …
• There are standard values for each of random forest hyperparameters recommended by long time practitioners
– But these parameters should be tuned through cross validation
(making them data and problem dependent)
– Through a grid search!!!
11
Variable Importance for RF
• Another drawback of bagging is…
– The averaged model is no longer easily interpretable!
→ No longer to trace the “logic” of an output through a series of
decisions based on predictor values
12
Variable Importance for RF
(Permutation Importance Case)
• Record the prediction accuracy on the out-of-bag samples for each tree
• Randomly permute the data for column j in the out-of-bag samples the
record the accuracy again
• The decrease in accuracy as a result of this permuting is averaged over
all trees, and is used as a measure of the importance of variable j in the
random forest
13
Some Thoughts on Random Forest
• Very popular in practice
– Probably the most popular classifier for dense data (≤ a few thousand
features)
• Easy to implement (train a lot of trees)
• Not quite state-of-the-art method!
– Boosted trees generally do better
• If the number of trees is too large, then the trees in the ensemble
may become more correlated, increase the variance
14
DEMO & PRACTICE
Practice Problem
• Objective: Building a learning model on breast cancer data
• Breast cancer (BC)
– One of the most common cancers among women worldwide
– Early diagnosis of BC can improve the prognosis and chance of
survival significantly
– Further accurate classification of benign tumors can prevent patients
undergoing unnecessary treatment
→ Classification and data mining methods are an effective way to
classify data
16
(FYI) Practice Problem (cont.)
• Recommended screening guidelines:
– Mammography – the most important screening test for breast
cancer is the mammogram. A mammogram is an X-ray of the breast.
It can detect breast cancer up to two years before the tumor can be
felt by you or your doctor
– Women age 40-45 or older who are at average risk of breast
cancer should have a mammogram once a year
– Women at high risk should have yearly mammograms along with
an MRI starting at age 30
17
Data
• Original data:
– Use the UCI machine learning repository for breast cancer dataset (569 patients)
– Is publicly available (was created by Dr.William H. Wolberg)
– Dr. Wolberg uses “fluid sample, taken from patients with “solid breast masses” and
analyzed cytological features based on digital scan
• Attribute information
– Diagnosis (M: Malignant; B: Benign) per each ID number
– For each cell nucleus, 10 features are computed
• Radius
• Texture
• Perimeter
• Area
• Smoothness
• Compactness
• Concavity
• Concave points
• Symmetry
• Fractal dimension
– Calculate mean, standard error, and worst or largest values
→ In total, for each patient, 30 features are calculated!!
18
Demo
• Questions:
– Develop a random forest model based on the data
– Calculate four evaluation measures (accuracy, precision, recall, and F1-
score) of the model
– Find the best-performed model by changing the parameters (# of trees : 20,
30, 40)
– Compare the evaluation measures with the ones learned before (logistic
regression and decision trees), which one performs the best?
19'''