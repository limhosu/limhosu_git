import FinanceDataReader as fdr
df = fdr.DataReader('001040', '2011-04-25', '2020-12-30')
print(df.head(10))
