# financedatareader로 데이터 가져오기
import pandas as pd
import FinanceDataReader as fdr
import seaborn as sns
import numpy as np
# df_krx = fdr.StockListing("KRX")
# df_krx.to_csv("d:/finance/krx.csv", index=False)
df = pd.read_csv("d:/finance/krx.csv")
df["ListingDate"]=pd.to_datetime(df["ListingDate"])

df["ListingYear"]=df["ListingDate"].dt.year
print(df[["ListingDate", "ListingYear"]])
# 테스트