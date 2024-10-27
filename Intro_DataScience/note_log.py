'''ML: Logistic Regression
College of Global Business
Hoon Jang
[GLOB 347] Lecture note #6
Agenda
• Overview of Logistic Regression
• Demo & Practice
2
Acknowledgements
All of the lecture notes for this class borrowed with/without modification from the sources
including lecture notes (prof. Tibshirani, G’Sell, Shalizi, Chouldechova, Franklin, etc.) and
books (Introduction to Business Analytics by Jaggia et al, etc.)
OVERVIEW OF LOGISTIC REGRESSION
Odds: Another Way of Quantifying the
Probability of Event
• Commonly used in gambling (and logistic regression!)
• Odds:
– For some event E,
– Similarly, if we are told the odds of E are x to y then
– Which implies
4
odds (E) = P(E) / P(Ec
)
odds (E) = x / y= {x / ( x+ y)} / {y / ( x+ y)}
P(E) = x / (x + y), P(Ec
) = y / (x + y)
Introductory Case: Donner Party
• In 1846 the Donner and Reed families left Springfield, Illinois, for
California by covered wagon. In July, the Donner Party, as it became
know, reached Fort Bridger, Wyoming. There its leaders decided to
attempt a new and untested rote to the Sacramento Valley. Having
reached its full size of 87 people and 20 wagons, the party was delayed
by a difficult crossing of the Wasatch Range and again in the crossing of
the desert west of the Grate Salt Lake. The group became stranded in
the eastern Sierra Nevada mountains when the region was hit by heavy
snows in late October. By the time the last survivor was rescued on April
21, 1847, 40 of the 87 members had died from famine and exposure to
extreme cold
5
Introductory Case: Data
• Data is given:
6
Introductory Case: Solution Approach
• Question:
– It seems clear that both age and gender have an effect on
someone’s survival, how do we come up with a model that will let us
explore this relationship?
• Solution Approach
– Even if we set Died to 0 and Survived to 1, this is not something we
can transform our way out of – we need something more
– One way to think about the problem:
• We can treat Survived and Died as successes and failures arising from
a binomial distribution where the probability of a success is given by a
transformation of a linear model of the predictors
7
Logistic Regression
• We assume a binomial distribution produced the outcome
variable and we therefore want to model p the probability of
success for a given set of predictors
• To finish specifying the logistic model we just need to
establish a reasonable link function
• There are a variety of options but the most commonly used
is the logit function:
8
Logit(p) = log (p / 1 – p), for 0 ≤ p ≤ 1
Properties of the Logit
• The logit function takes a value between 0 and 1 and maps
it to a value between −∞ and +∞
• Therefore, the inverse logit function takes a value between
− ∞ and +∞ and maps it to a value between 0 and 1
– This formulation also has some use when it comes to interpreting
the model as logit can be interpreted as the log odds of a success,
more on this later
9
G-1
(x) = exp(x) / {1 + exp(x)} = 1 / {1 + exp(-x)}
Logistic Regression: Mathematical Derivation
• The logistic regression model constrains the probabilities to
be between 0 and 1: 𝑝
Ƹ
=
exp(𝑏0+𝑏1𝑥)
1+exp(𝑏0+𝑏1𝑥)
– This allows for a nonlinear relationship
– The model is estimated by Maximum Likelihood Estimation
10
Back to the Introductory Case: Results
• Regression results:
– Use only “age” as a single predictor
11
Back to the Introductory Case: Results
• Regression results:
– Odds: Probability of survival for a 25-year-old person:
– Odds: Probability of survival for a 50-year-old person:
12
Back to the Introductory Case: Interpretation
• Simple interpretation is only possible in terms of log odds
and log odds ratio for intercept and slope terms
• Intercept: The log odds of survival for a party member with
an age of 0
– From this we can calculate the odds or probability, but additional
calculations are necessary
• Slope: For a unit increase in age (being 1 year older) how
much will the log odds ratio change, not particularly intuitive
– More often then not we care only about sign and relative magnitude
13
Back to the Introductory Case: Interpretation
• Log odds of the slope:
14
What does this mean by that?
Statistical Testing for the Slope of Age
• Use z-value to check whether statistically valid
15
Logistic Regression: Application
• Logistic regression is probably the most widely used
general-purpose classifier
• Its very scalable and can be very fast to train. It’s used for
– Spam filtering
– News message classification
– Web site classification
– Product classification
– Most classification problems with large, sparse feature
sets
• The only caveat is that it can overfit on very sparse data,
so its often used with “Regularization” technique
16
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
18
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
19
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
20
Demo
• Questions:
– Build a regression model
– Evaluate the model using four evaluation measures (accuracy, precision,
recall, and F1-score)
– See what happens if you increase the volume of “test dataset” (Default = 0.3)
21'''