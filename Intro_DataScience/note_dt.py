'''ML: Classification (Decision Tree)
College of Global Business
Hoon Jang
[GLOB 347] Lecture note #7
Agenda
• What is Decision Tree?
• Learning Decision Trees
• Demo & Practice
2
Acknowledgements
All of the lecture notes for this class borrowed with/without modification from the sources
including lecture notes (prof. Tibshirani, G’Sell, Shalizi, Chouldechova, Franklin, etc.) and
books (Introduction to Business Analytics by Jaggia et al, etc.)
WHAT IS DECISION TREE?
Other Classification Techniques
• We learned about linear classification method (e.g., logistic
regression)
• Any other idea?
– Pick an attribute, do a simple test
– Conditioned on a choice, pick another attribute, do another test
– In the leaves, assign a class with majority vote
– Do other branches as well
• Reasonable?
4
Idea on Decision Tree
• Give axes aligned decision boundaries
5
Idea on Decision Tree (cont.)
6
• Here is a test example, then?
7cm
10 cm
Decision Trees
• A decision tree is a graphical depiction of a decision and
every potential outcome or result of making that decision
– It gives people an effective and easy way to visualize and
understand the potential options of a decision and its range of
possible outcomes
• Properties
– Branching is determined by attribute value
– Leaf nodes are outputs (class assignment)
7
Decision Trees: Simple Rules
• Choose an attribute on which to descend at each level
• Condition on earlier (higher) choices
• Generally, restrict only one dimension at a time
• Declare an output value when you get to the bottom
• In the previous example, we only split each dimension once,
but that is not required
8
LEAERNING DECISION TREES
Learning Decision Trees
• Learning the simplest decision tree is “very difficult problem”
– If there are k features, a decision tree might have up to 2
k nodes
– This is usually much too big in practice
→We want to find “efficient” (smaller) trees
• Resort to a greedy heuristic:
– Start from an empty decision tree
– Split on next best attribute
→ Do this in a greedy manner by recursively choosing a best split
feature at each node
10
How to Choose a Good Attribute?
• Main Idea: A good feature splits the examples into subsets
that are (ideally) "all positive" or "all negative“
– All classes in leaf equally probable → Bad!
• Technically, we will use Entropy!
11
Information Theory
• Entropy is the average level of information inherent in the
variable’s possible outcomes
– pi be the fraction of examples in class i
12
𝐸 = −෍
𝑖=1
𝑚
𝑝𝑖
log 𝑝𝑖
Information Gain
• Before split by f, the entropy is:
• After split by f, the entropy is:
– Let 𝑝𝑖
𝑓
be the fraction of elements with feature f that lie in class i
– Let 𝑝𝑖
−𝑓
be the fraction of elements without feature f that lie in class i
• The information gain = 𝐸 − 𝐸𝑓 (Information = –entropy)
13
𝐸 = −෍
𝑖=1
𝑚
𝑝𝑖
log 𝑝𝑖
𝐸𝑓 = −𝑝
𝑓 ෍
𝑖=1
𝑚
𝑝𝑖
𝑓
log 𝑝𝑖
𝑓 − 𝑝
−𝑓෍
𝑖=1
𝑚
𝑝𝑖
−𝑓
log 𝑝𝑖
−𝑓
Example
• Using four features (“Outlook”, “ Temperature”, “Humidity”,
“Windy”), estimate whether go play
– Parent’s entropy
14
Entropy (Play)
= (-5/14 log2
(5/14)) + (-9/14 log2
(9/14)
= 0.94
Example
• Using four features (“Outlook”, “ Temperature”, “Humidity”,
“Windy”), estimate whether go play
– Children’s entropy
15
Entropy (Play, Outlook)
= P(sunny) * E(Play) + P(overcast) * E(Play) +
P(rainy) * E(play)
= 5/14 * [(-3/5 log2
(3/5)) + (-2/5 log2
(2/5)] +
4/14 * [(-4/4 log2
(4/4))] +
5/14 * [(-3/5 log2
(3/5)) + (-2/5 log2
(2/5)] +
= 0.69
Information gain = 0.94 – 0.69 = 0.25
Entropy (Play, Outlook)
= P(true) * E(Play) + P(false) * E(Play)
= 0.89
Information gain = 0.94 – 0.89 = 0.05
Choosing the Best Feature
• At each node, we choose the feature f which maximizes
the information gain
• This tends to be produced mixtures of classes at each node
that are more and more “pure” as you go down the tree
• If a node has examples all of one class c, we make it a leaf
and output “c”. Otherwise, when we hit the depth limit, we
output the most popular class at that node
16
Constructing Decision Trees
• We made the fruit data partitioning just by eyeballing it
• Instead, we can use the “information gain” to automate the
process. At each level, one must choose:
– Which variable to split
– Possible where to split it
• Choose them based on how much information we would
gain from the decision!
– i.e., Choose attribute that gives the highest gain
17
Decision Tree Algorithm
• Simple, greedy, recursive approach, builds up tree node-bynode
– Step 1: Pick an attribute to split at a non-terminal node
– Step 2: Split examples into groups based on attribute value
– Step 3: For each group:
• If no examples: Then, return majority from parent → Stop
• Else if all examples in same class: Return class → Stop
• Else Loop to Step 1
• Early stopping criteria
– Restrict the tree depth to a certain level
– Restrict the minimum number of observations allowed in any
terminal node
18
Decision Tree is Almighty?
• Though efficient, there are “MANY” problems
– You have exponentially less data at lower levels
– Too big of a tree can overfit the data
– Greedy algorithms don’t necessarily yield the global optimum
• Any other alternatives?
19
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
21
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
22
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
23
Demo
• Questions:
– Develop a decision tree model based on the data
– Calculate four evaluation measures (accuracy, precision, recall, and F1-
score) of the model
– Compare the evaluation measures with the ones from the logistic regression,
which one is better?
24'''