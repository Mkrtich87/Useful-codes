import numpy as np
import pandas as pd
from pandas_datareader import data as wb
tickers=['PG','MSFT','T','F','GE']
new_data=pd.DataFrame()
for t in tickers:   
    new_data[t]= wb.DataReader(t, data_source='iex', start='2015-1-1')['Adj close']
new_data.tail()