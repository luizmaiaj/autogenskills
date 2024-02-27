import requests
import pandas as pd
from datetime import date, timedelta
from io import StringIO

# Define a function to get the stock data
def get_stock_data(symbol):
    from datetime import datetime
    
    start_date = (date.today()-timedelta(days=365))
    end_date = date.today()
    
    start_timestamp = int(datetime.timestamp(start_date))
    end_timestamp = int(datetime.timestamp(end_date))
    url = f"https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={start_timestamp}&period2={end_timestamp}&interval=1d&events=history&includeAdjustedClose=true"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    df = pd.read_csv(StringIO(response.text))
    return df

# Get historical stock prices for NVDA and TESLA from Yahoo Finance
nvda_df = get_stock_data('NVDA')
tesla_df = get_stock_data('TSLA')
# Plot the chart
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(pd.to_datetime(nvda_df['Date']), nvda_df['Adj Close'], label='NVDA')
ax.plot(pd.to_datetime(tesla_df['Date']), tesla_df['Adj Close'], label='TSLA')
ax.set_xlabel('Date')
ax.set_ylabel('Adjusted Close Price ($)')
ax.legend()
fig.savefig("nvda_tesla.png")