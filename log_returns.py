#Lesson 65 log return
#Obtaining info
#Calculating simple return
#Plotting
import pandas
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
PG=wb.DataReader("PG",data_source="yahoo",start='1995-1-1')
print(PG.head())
PG['Log_return']=np.log(PG['Adj Close']/PG['Adj Close'].shift(1))
PG['Log_return'].plot(figsize=(8,5))
plt.figure()
log_return_d=PG['Log_return'].mean()
log_return_a=PG['Log_return'].mean()*250
print(log_return_d)
print(log_return_a*100)