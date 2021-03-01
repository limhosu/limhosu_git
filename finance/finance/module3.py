import FinanceDataReader as fdr
import pandas as pd
import FinanceDataReader as fdr
import seaborn as sns
import numpy as np
#df = fdr.DataReader('001040', '2011-04-25', '2020-12-30')
#print(df.head(10))


# 삼성전자(005930) 전체 (1996-11-05 ~ 현재)

df = fdr.DataReader('005930', '2020-01-01', '2020-02-15')

fdr.chart.plot(df)
fdr.chart.plot(df, title='삼성전자(005930)')
print(df)

