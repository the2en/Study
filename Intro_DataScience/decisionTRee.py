import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
import graphviz

# 1. read dataset
df = pd.read_csv('./data/train.csv', header=0)

# 2. make dummies
df['Sex'] = df['Sex'].astype('category')
df['Embarked'] = df['Embarked'].astype('category')
df['Pclass'] = df['Pclass'].astype('category')
df = pd.get_dummies(df)

# 3. data splitting
Y = df['Survived']
X = df.loc[:, ~df.columns.isin(['Survived'])]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# 4. model fitting and predition
dt_model = DecisionTreeClassifier()    # criterion, max_depth, min_samples_splits
dt_model.fit(X_train, Y_train)
Y_pred = dt_model.predict(X_test)

# 5. performance evaluation
confusion_matrix = confusion_matrix(Y_test, Y_pred)
accuracy = accuracy_score(Y_test, Y_pred)
precision = precision_score(Y_test, Y_pred)
recall = recall_score(Y_test, Y_pred)

print('Acc: {0:.3f}, Precision: {1:.3f}, Recall: {2:.3f}'.format(accuracy, precision, recall))

# Visualization of decision tree
dot_data = export_graphviz(dt_model, out_file=None, feature_names=X.columns, class_names=['Not Survived', 'Survived'], filled=True)
graph = graphviz.Source(dot_data)
graph.render("decision_tree")  # Save the decision tree diagram to a file
graph.view()  # Display the decision tree diagram