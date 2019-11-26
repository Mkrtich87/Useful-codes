# less66
# simple portfolio of 4 assets with equal weights

import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
tickers = ['PG', 'MSFT', 'F','GE']
mydata = pd.DataFrame()
for t in tickers:  
    mydata[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']   
mydata.info()
print(mydata.head())
print(mydata.tail())
print(mydata.iloc[0])
(mydata/mydata.iloc[0]*100).plot(figsize = (15,6))
plt.show()
mydata.plot(figsize=(16,6))
plt.show()
mydata.loc['1995-1-3']
mydata.iloc[0]
returns = (mydata/mydata.shift(1))-1
returns.head()
weights = np.array([0.25, 0.25, 0.25, 0.25])
np.dot(returns,weights)
annual_returns = returns.mean()*250
print(annual_returns)
np.dot(annual_returns,weights)
portfolio_1=str(round(np.dot(annual_returns,weights),5)*100)+'%'
print(portfolio_1)