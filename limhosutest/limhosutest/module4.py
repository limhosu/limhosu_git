from openpyxl import load_workbook
import datetime
from datetime import date
from datetime import timedelta
import pandas as pd
import numpy as np
import csv
import os
wb1 = "d:/limhosu/limhosutest/limhosutest/test1.xlsx"
data1 = pd.read_excel(wb1)                      
print(data1)
wb2 = "d:/limhosu/limhosutest/limhosutest/test2.xlsx"
data2 = pd.read_excel(wb2)
print(data2)
dataall = data1.merge(data2,how='left', on=['날짜', '동','호수'])
print(dataall)
