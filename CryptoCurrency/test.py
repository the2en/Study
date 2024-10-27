import pandas as pd
import matplotlib.pyplot as plt

# Ether(ETH_KR) price from Bithumb(KR exchange)
df = pd.read_csv('Ether_KR.csv')

print(df.dtypes)
df['Date'] = pd.to_datetime(df.Date,
                            format='%m/%d/%Y')
df.Price.replace({',':''}, regex=True, inplace=True)
df['Price'] = df.Price.astype(float)

df = df[['Date', 'Price']]

# FX rate

dfx = pd.read_csv('USD_KRW Historical Data.csv')
dfx['Date'] = pd.to_datetime(df.Date,
                             format='%m/%d/%Y')
dfx.Price.replace({',':''}, regex=True, inplace=True)
dfx['FX'] = dfx.Price.astype(float)

dfx = dfx[['Date', 'FX']]

# Q1: Merge it with FX rate
df = pd.merge(df, dfx, how='left', on='Date')

# Q2: Convert ETH_KR into USD
df['Bithum(USD)'] = df.Price*(1/df.FX)

# Price at exchanges abroad
dfy = pd.read_csv('ETH_USD Binance Historical Data.csv')
dfy['Date'] = pd.to_datetime(df.Date,
                             format='%m/%d/%Y')
dfy.Price.replace({',':''}, regex=True, inplace=True)
dfy['Price'] = dfy.Price.astype(float)

dfy = dfy[['Date', 'Price']]
dfy.rename(columns={'Price':'Binance'}, inplace=True)
df = pd.merge(df, dfy, how='left', on='Date')

df['overval'] = df['Bithum(USD)'] - df.Binance
print(df.overval.describe())

plt.plot(df.Date, df.Binance, drawstyle='steps',
         color='black', linewidth=1)
plt.fill_between(df.Date, df['Bithum(USD)'], df.Binance,
                 step='pre', color='orange')
plt.show()
# Q3: Merge it with ETH_US (Ether price from Binance)
# Q4: Calculate Kimchi Premium(ETH_KR in ISD - ETH_US) for Ether
# Q5: Get descriptive stats for the Kimchi Premium