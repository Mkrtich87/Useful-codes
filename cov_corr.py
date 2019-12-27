"""Lesson 71 Calculating the Risk of a Security"""
import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
tickers = ['PG', 'BEI.DE']
sec_data = pd.DataFrame()
for t in tickers:
    sec_data[t]=wb.DataReader(t,data_source='yahoo', start = '2007-1-1')["Adj Close"]
print(sec_data.tail())
sec_returns = np.log(sec_data/sec_data.shift(1))
print(sec_returns)
#PG
print(sec_returns['PG'].mean())
print(sec_returns['PG'].mean()*250)
print(sec_returns['PG'].std())
print(sec_returns['PG'].std()*250*0.5)

#Beirsdorf
print(sec_returns['BEI.DE'].mean())
print(sec_returns['BEI.DE'].mean()*250)
print(sec_returns['BEI.DE'].std())
print(sec_returns[['PG','BEI.DE']].std()*250*0.5)

pg_var = sec_returns["PG"].var()
print("PG VARIANCE")
print(pg_var*250)
bei_var = sec_returns['BEI.DE'].var()
print("BE VARIANCE")
print(bei_var*250)
cov_matrix = sec_returns.cov()
print(cov_matrix)
cov_matrix = sec_returns.cov()*250
print(cov_matrix)
corr_matrix = sec_returns.corr()
print(corr_matrix)
