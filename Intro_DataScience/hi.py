import pandas as pd

df = pd.read_csv("./data/Midterm.csv", header = 0)

# 데이터프레임의 복사본 생성
# 복사본의 가공은 원본 데이터에 영향을 주지 않는다.
data = df.copy()

# 조건식을 만족하는 자료만 필터링한 데이터프레임 생성
data1 = data.query('조건식')

pd.crosstab(index=df[범주변수], columns=열레이블)