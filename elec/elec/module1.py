import pandas as pd
import numpy as np
import openpyxl


elec = pd.read_excel('d:/전기수도계산/수도요금/2020년09월.xlsx', sheet_name='Sheet1', skiprows = 5, )
print(elec.fillna(5))
elec=elec.iloc[:,:4]

elec.rename(columns={elec.columns[0]:'동',
                     elec.columns[1]:'삭제',
                     elec.columns[2]:'호',
                     elec.columns[3]:'전월'},inplace=True)
elec=elec[['동','호','전월']]
elec=elec[elec.동!='동']
elec=elec[elec.동!='동계']
elec=elec[elec.동!='합계']

elec=elec[elec.호>0]
elec=elec.fillna(method='ffill')

elec.to_excel('d:/전기수도계산/수도요금/2020년09월연습.xlsx')