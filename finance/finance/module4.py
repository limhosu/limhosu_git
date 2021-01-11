from pykrx import stock
tickers = stock.get_market_ticker_list("20190225")
print(tickers)
df = stock.get_market_ohlcv_by_date("20180810", "20201212", "005930", "m")
print(df.head(3))