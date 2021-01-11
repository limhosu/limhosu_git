import pandas_datareader as pdr
samsung=pdr.get_data_yahoo('005930.KS', start='2011-08-19', end='2021-01-10')
print(samsung)
samsung.to_excel('d:/finance/samsung.xlsx')
