import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OneHotEncoder

# 데이터 불러오기
df = pd.read_csv('C:/Users/USER/Desktop/DataScience file/Team Project/superstore_data.csv')

# One-hot 인코딩 적용
categorical_cols = ['Education', 'Marital_Status']
one_hot_encoder = OneHotEncoder(sparse=False)
one_hot_encoded = one_hot_encoder.fit_transform(df[categorical_cols])
one_hot_encoded_df = pd.DataFrame(one_hot_encoded, columns=one_hot_encoder.get_feature_names_out(categorical_cols))
df = pd.concat([df.drop(categorical_cols, axis=1), one_hot_encoded_df], axis=1)

# 데이터를 features와 target으로 나눔
features = df.drop(['Response'], axis=1)
target = df['Response']

# 데이터를 training set과 test set으로 나눔
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Random Forest 모델 생성
rf = RandomForestClassifier(random_state=42)

# GridSearchCV를 이용해 하이퍼파라미터 튜닝
param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [3, 5, 7, 10]}
clf = GridSearchCV(rf, param_grid=param_grid, cv=5)
clf.fit(X_train, y_train)

# 선택된 하이퍼파라미터 확인
print("Best parameters: ", clf.best_params_)

# 모델 평가
y_pred = clf.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification report:\n", classification_report(y_test, y_pred))
