import pandas as pd

df = pd.read_excel('entalk.xlsx')

print(df.dtypes)
print(df['종류'].value_counts())

df = df.drop(['상태', '접수일자', '완료일자', '입금', '정발', '송금', '역발', '회사명', '고객명'], axis='columns')

# 각각 데이터프레임 제작
HMI_df = df[(df['종류'] == '모니터/터치판넬/HMI')]
HMI_df = pd.concat([HMI_df, df[(df['종류'] == 'HMI')]])

controller_df = df[df['종류'] == '컨트롤러']

print(controller_df)
print(controller_df['수리내역'].value_counts())