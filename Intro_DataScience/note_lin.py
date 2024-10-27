'''ML: Regression
College of Global Business
Hoon Jang
[GLOB 347] Lecture note #5
Agenda
• Overview of Linear Regression
• Three Issues of Linear Regression
• Demo & Practice
2
Acknowledgements
All of the lecture notes for this class borrowed with/without modification from the sources
including lecture notes (prof. Tibshirani, G’Sell, Shalizi, Chouldechova, Franklin, etc.) and
books (Introduction to Business Analytics by Jaggia et al, etc.)
OVERVIEW OF LINEAR REGRESSION
Introductory Case: College Scorecard
• Which college factors influence post-college earnings?
– If a college costs more or has a higher graduation rate, should a student expect to
earn more after graduation?
– If a greater percentage of the students are paying down debt after college, does this
somehow influence post-college earnings?
– And finally, does the location of a college affect post-college earnings?
• Data from 116 colleges on the following variables:
– Annual post-college earnings (Earnings in $)
– The average annual cost (Cost in $)
– The graduation rate (Grad in %)
– The percentage of students paying down debt (Debt in %)
– Whether or not a college is located in a city (City equals 1 if a city location, 0
otherwise)
4
The Linear Regression Model: Overview
• Regression analysis captures the relationship between two
or more variables
– Predict an outcome of a target variable based on several input
variables
– Determine which input variables matter the most
– Determine which input variables we can ignore
– Describe and/or predict changes in the target variable based on
changes in the input variables
5
The Linear Regression Model: Overview
• A linear regression model postulates that the relationship
between the response and predictors is linear
– The target or response is denoted as 𝑦
– The input or predictor variables are denoted as 𝑥1, 𝑥2, ⋯ , 𝑥𝑘
6
The Linear Regression Model: Variable
• A regression model treats all predictor variables as numerical
• A numerical variable assumes meaningful numeric values
• A categorical variable reflects categories
• A dummy variable is used to describe two categories of a
categorical variable, denoted 𝑑
– Indicator or binary variable
– 𝑑 = 1 for one of the categories
– 𝑑 = 0 for the other(s)
• Reference or benchmark category
• All comparisons are made relative to this category
– Example: City is 1 if a city location, 0 otherwise
7
A Simple Linear Regression Model
• It uses only one predictor variable:
𝑦 = 𝛽0 + 𝛽1𝑥1 + 𝜀
– 𝛽0 is the unknown intercept
– 𝛽1 is the unknown slope
– 𝛽0 + 𝛽1𝑥1 is the deterministic component
– 𝜀 is the stochastic component or random error term
8
Multiple Linear Regression Model
• It uses more than one predictor:
𝑦 = 𝛽0 + 𝛽1𝑥1 + 𝛽2𝑥2 + ⋯ + 𝛽𝑘𝑥𝑘 + 𝜀
– Replace 𝑥 with 𝑑 for a dummy variable
• The population parameters 𝛽0, 𝛽1, 𝛽2, … , 𝛽𝑘 are unknown and
must be estimated using sample data
• Sample data: 𝑛 observations of 𝑦, 𝑥1, 𝑥2, … , 𝑥𝑘
• Use the sample data to obtain 𝑏0, 𝑏1, 𝑏2, … 𝑏𝑘 which are estimates
of 𝛽0, 𝛽1, 𝛽2, … , 𝛽𝑘
9
(Optional) Least Square Method
• A form of mathematical regression analysis used to
determine the line of best fit for a set of data, providing a
visual demonstration of the relationship between the data
points
10
(Optional) Demo (Least Square Method)
x y (x - ഥ𝒙) (y - 𝒚) (x - ഥ𝒙)
2
(x - ഥ𝒙) (y - 𝒚)
1 2
2 4
3 5
4 4
5 5
11
0
0.2
0.4
0.6
0.8
1
1.2
0 0.2 0.4 0.6 0.8 1 1.2
Estimation of Regression Coefficients
• It is important to interpret the estimated regression coefficients
• 𝑏0 is the estimate of 𝛽0
– Predicted value of 𝑦ො when each predictor variable assumes a value
of 0
– Not always meaningful
• 𝑏𝑗
is the estimate of 𝛽𝑗
– Change in the predicted value of the response given a unit increase
in 𝑥𝑗
, holding all other predictor variables constant
– Partial influence of 𝑥𝑗 on 𝑦ො
12
Back to Introductory Case:
• Example: 𝐸𝑎𝑟𝑛𝑖𝑛𝑔𝑠 = 𝛽0 + 𝛽1𝐶𝑜𝑠𝑡 + 𝛽2𝐺𝑟𝑎𝑑 + 𝛽3𝐷𝑒𝑏𝑡 + 𝛽4𝐶𝑖𝑡𝑦 + 𝜀
• Questions:
– What is the sample regression equation?
– Interpret the slope coefficients
– Predict the annual post-college earnings if a college’s average annual cost is $25,000,
its graduation rate is 60%, its percentage of students paying down debt is 80%, and it
is located in a city.
13
Regression Results:
14
Answers to the Questions
• 𝐸𝑎𝑟𝑛𝑖𝑛𝑔𝑠 ෣ = 10004.97 + 0.4349𝐶𝑜𝑠𝑡 + 178.10𝐺𝑟𝑎𝑑 + 141.48𝐷𝑒𝑏𝑡 +
+ 2526.79𝐶𝑖𝑡𝑦
• All coefficients are positive, suggesting a positive influence of each
predictor variable on the response variable
– Holding all other predictor variables constant, if the average annual
costs increase by $1, then, on average, predicted earnings are
expected to increase by $0.4349
– All else constant, predicted earnings are $2,526.79 higher for
graduates of colleges located in a city
• 𝐸𝑎𝑟𝑛𝑖𝑛𝑔𝑠 ෣ = 10,004.97 + 0.434 ∗ 25,000 + 178.10 ∗ 60 + 141.48 ∗ 80 +
+ 2,526.79 ∗ 1 = 45,408.7991 or about $45,409
15
Modeling Categorical Variables
• A categorical variable may be defined by more than two categories
• Use multiple dummy variables to capture all categories, one for each
category
• Given the intercept term, we exclude one of the dummy variables from
the regression
– The excluded variable represents the reference category
– Including all dummy variables creates perfect multicollinearity
• Example) Mode of transportation with three categories
– Public transportation, driving alone, or car pooling
– 𝑑1 = 1 for public transportation and 0 otherwise
– 𝑑2 = 1 for driving alone and 0 otherwise
– 𝑑1 = 𝑑2 = 0 indicates car pooling
16
Example: With Dummy Variables
• Example: Retail sales, the gross national product (GNP), Quarter
• Questions:
– Estimate 𝑦 = 𝛽0 + 𝛽1𝑥 + 𝛽2𝑑1 + 𝛽3𝑑2 + 𝛽4𝑑3 + 𝜀, where 𝑦 and 𝑥 are
sales and GNP, 𝑑1is a quarter 1 dummy, 𝑑2 is a quarter 2 dummy,
and 𝑑3 is a quarter 3 dummy
– Interpret the slope coefficient for quarter 1
– What are the predicted sales in quarter 2 if GNP is $18,000 (in
billions)?
17
Answers to the Questions:
• Regression results (from statistical software)
• All else equal, retail sales in quarter 1 are expected to be approximately
$108,765 million less than sales in quarter 4 (d1
, d2
, d3 = 0)
• 𝑥 = 18,000, 𝑑1 = 0, 𝑑2= 1, 𝑑3= 0 so that 𝑦ො = $1,187,595. Retail sales
are predicted to be approximately $1,187,595 (in millions) in the second
quarter when the GNP is $18,000 (in billions)
18
Post Lecture Activity
• Solve the following problem
19'''