from pykrx import stock
import time
df = stock.get_market_ohlcv_by_ticker("20200831")
print(df.tail())

