import btalib
import pandas as pd

df = pd.read_csv('data/ohlc/AAPL.txt', parse_dates=True, index_col='Date')

sma = btalib.sma(df, period=5)

rsi = btalib.rsi(df)

df['sma'] = sma.df
df['rsi'] = rsi.df

oversold_days = df[df['rsi'] < 30]

print(oversold_days)