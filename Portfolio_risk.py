# 77 Calculating Portfolio risk
#nump dot notation for vector multiplication
import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
tickers = ['aapl', 'msft']
sec_data = pd.DataFrame()
for t in tickers:
    sec_data[t]=wb.DataReader(t,data_source='yahoo', start = '2007-1-1')["Adj Close"]
print(sec_data.tail())
sec_returns = np.log(sec_data/sec_data.shift(1))
print(sec_returns)
weights = np.array([0.5,0.5])
#Portfolio Variance
pfolio_var=np.dot(weights.T, np.dot(sec_returns.cov()*250, weights))
print("Portfolio Variance")
print(pfolio_var)
#Portfolio Volatilty
print("Portfolio Volatilty")
pfolio_vol=np.dot(weights.T, np.dot(sec_returns.cov()*250, weights))**0.5
print(pfolio_vol)
print(str(round(pfolio_vol,5)*100) +'%')
