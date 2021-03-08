import yfinance as yf
import pandas as pd

#data = yf.download("MSFT",period="7d",interval="1m")

stocks = ["AMZN","MSFT","INTC","GOOG","INFY.NS","3988.HK"]
start = dt.datetime.today() - dt.timedelta(360)
end = dt.datetime.today()
cl_price = pd.DataFrame()
ohlcv_data = {} #empty dictionary which will be filled with ohlcv dataframe for each ticker