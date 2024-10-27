import pandas as pd
import matplotlib.pyplot as plt

# Ether(ETH_KR) price from Upbit(KR exchange)
df = pd.read_csv('./data/ADA_KRW Upbit Historical Data.csv')

# Date, Price, Change % type change
df['Date'] = pd.to_datetime(df.Date, format='%m/%d/%Y')
df.Price.replace({',':''}, regex=True, inplace=True)
df['Price'] = df.Price.astype(float)

# Remove % and then change type
df['Change %'] = df['Change %'].str.replace('%', '')
df['Change %'] = df['Change %'].astype(float)

# Upbit data
dfu = df[['Date', 'Price']]

# Search max and min change date
max_index = df['Change %'].idxmax()
min_index = df['Change %'].idxmin()
max_date = df.loc[max_index, 'Date']
min_date = df.loc[min_index, 'Date']

# Visualization
plt.plot(df.Date, df.Price)
plt.plot(df.loc[max_index, 'Date'], df.loc[max_index, 'Price'], 'r-', label='Max')
plt.plot(df.loc[min_index, 'Date'], df.loc[min_index, 'Price'], 'b-', label='Min')
plt.title('Daily Market Price of ADA')
plt.show()

# FX rate
dfx = pd.read_csv('./data/USD_KRW Historical Data.csv')
dfx['Date'] = pd.to_datetime(dfx.Date, format='%m/%d/%Y')
dfx.Price.replace({',':''}, regex=True, inplace=True)
dfx['FX'] = dfx.Price.astype(float)

dfx = dfx[['Date', 'FX']]

# Merge it with FX rate
data = pd.merge(dfu, dfx, how='left', on='Date')

# Q2: Convert ETH_KR into USD
data['Upbit(USD)'] = data.Price*(1/data.FX)

# Price at exchanges abroad
dfy = pd.read_csv('./data/ADA_USD Binance Historical Data.csv')
dfy['Date'] = pd.to_datetime(dfy.Date, format='%m/%d/%Y')
dfy.Price.replace({',':''}, regex=True, inplace=True)
dfy['Price'] = dfy.Price.astype(float)

dfy = dfy[['Date', 'Price']]
dfy.rename(columns={'Price':'Binance'}, inplace=True)
data = pd.merge(data, dfy, how='left', on='Date')

data.dropna(inplace=True)

data['overval'] = data['Upbit(USD)'] - data.Binance
print(data.overval.describe())

plt.plot(data.Date, data.Binance, drawstyle='steps',
         color='black', linewidth=1)
plt.fill_between(data.Date, data['Upbit(USD)'], data.Binance,
                 step='pre', color='orange')
plt.title('Kimchi Premium of ADA')
plt.show()