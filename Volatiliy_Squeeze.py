
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web


# In[14]:


def get_adj_close(ticker, start, end):
    start = start
    end = end
    info = web.DataReader(ticker, data_source='yahoo', start=start, end=end)['Adj Close']
    return pd.DataFrame(info)

def bollinger_band(ticker, start, end):
    tick = get_adj_close(ticker, start, end)
    tick['30 Day MA'] = tick['Adj Close'].rolling(window=20).mean()
    tick['30 Day STD'] = tick['Adj Close'].rolling(window=20).std()
    tick['Upper Band'] = tick['30 Day MA'] + (tick['30 Day STD']*2)
    tick['Lower Band'] = tick['30 Day MA'] - (tick['30 Day STD']*2)
    
    tick[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
    plt.title('30 Day Bollinger Band for ' + str(ticker))
    plt.ylabel('Price (USD)')
    plt.show()

bollinger_band('fb', '1/2/2016', '31/12/2017')

