#네이버에서 ETF전종목 수집 JSON타입도 판다스로
import pandas as pd
import numpy as np
import requests
url = "https://finance.naver.com/api/sise/etfItemList.nhn?etfType=0&targetColumn=market_sum&sortOrder=desc"
response = requests.get(url)
etf_json = response.json()
etfItemList = etf_json["result"]['etfItemList']
print(len(etfItemList))
df = pd.DataFrame(etfItemList)
print(df)
import datetime
today = datetime.datetime.today()
today = today.strftime("%Y-%m-%d")
print(today)
file_name = f"eft_{today}_raw.csv"
print(file_name)
df.to_csv(file_name, index=False)



