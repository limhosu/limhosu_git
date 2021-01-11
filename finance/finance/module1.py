import pandas as pd
import requests
import io
import tqdm
from io import BytesIO
import time
import json
import numpy as np
import datetime
from bs4 import BeautifulSoup
import math
pd.options.display.float_format = '{:.2f}'.format
url = 'https://kind.krx.co.kr/corpgeneral/corpList.do' 
data = {
  'method':'download',
  'orderMode':'1',             #정렬할 컬럼
  'orderStat':'D',             #내림차순
  'searchType':'13',           #검색유형(상장법인)
  'fiscalYearEnd':'all',       #결산월(전체)
  'location':'all',            #지역(전체)
 }


#데이터 가저오기
r = requests.post(url, data=data)
i = BytesIO(r.content)
df = pd.read_html(i, header=0)
df_clean = df[0].copy()

#종목코드 자리수 채우기
df_clean['종목코드'] = df_clean['종목코드'].astype(np.str) 
df_clean['종목코드'] = df_clean['종목코드'].str.zfill(6)
df_clean

# srim 기초데이터프레임
srim = df_clean[['종목코드','회사명','업종']]
srim = srim.set_index('종목코드')
srim['계산일자'] = datetime.datetime.now().strftime('%Y-%m-%d')
srim['지배주주지분'] = None
srim['ROE'] = None
srim['기대수익률'] = None
srim['발행주식수_보통주'] = None
srim['발행주식수_우선주'] = None
srim['발행주식수_우선주'] = None
srim['S-RIM'] = None
srim['S-RIM_-10%'] = None
srim['S-RIM_-20%'] = None
srim['매도주가'] = None
srim['적정주가'] = None
srim['매수주가'] = None
srim['최근종가'] = None


srim
# 원하는 종목명 입력, 만약 상장사 전체를 계산할 경우 주석처리
stock_names = ['삼성전자','대한항공','하림지주',
               '삼양사', '카카오', 'SK하이닉스', 'LG화학']

srim_df = pd.DataFrame()
for stock_name in stock_names:
    srim_df = srim_df.append(srim.loc[srim['회사명'].str.contains(stock_name)])

# 원하는 종목명 입력, 만약 상장사 전체를 계산할 경우 주석처리 해제 
#srim_df = srim.copy()

srim_df
stock_codes = srim_df.index.to_list()

for stock_code in tqdm.tqdm(stock_codes):
    time.sleep(1)
    try:
        # fnguide 정보수집(맥쿼리 인프라와 같은 금융회사는 재무정보 제공되지 않음, 차기 추정 ROE가 없는 경우도 있음, 완전자본잠식에 의한 값이 없을수있음)
        url = 'http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A{}&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701'.format(stock_code)
        r = requests.get(url)
        df_finance = pd.read_html(r.text,match = '지배주주지분')  
        df_finance = df_finance[0].copy()
        df_finance = df_finance.iloc[:,:5]
        
        # 기본적으로 fnguide에서 추정한 자본을 사용하는데 없을 경우 최근 결산일의 자룔를 사용
        srim_df.loc[stock_code,'지배주주지분'] = df_finance.loc[df_finance[df_finance.columns[0]] == '지배주주지분',df_finance.columns[-1]].values[0]
        if math.isnan(srim_df.loc[stock_code,'지배주주지분']) == True:
            srim_df.loc[stock_code,'지배주주지분'] = df_finance.loc[df_finance[df_finance.columns[0]] == '지배주주지분',df_finance.columns[-2]].values[0]
        else:
            pass

        # 기본적으로 추정 ROE를 사용하는데 없을경우 3개년 가중평균 사용
        srim_df.loc[stock_code,'ROE'] = df_finance.loc[df_finance[df_finance.columns[0]] == 'ROE',df_finance.columns[-1]].values[0]
        if math.isnan(srim_df.loc[stock_code,'ROE']) == True:
            roe1 = df_finance.loc[df_finance[df_finance.columns[0]] == 'ROE',df_finance.columns[-2]].values[0]
            roe2 = df_finance.loc[df_finance[df_finance.columns[0]] == 'ROE',df_finance.columns[-3]].values[0]
            roe3 = df_finance.loc[df_finance[df_finance.columns[0]] == 'ROE',df_finance.columns[-4]].values[0]

            for num,i in enumerate([roe3,roe2,roe1]):
                if num == 0:
                    if i !="완전잠식":
                        if math.isnan(i) == True:
                            total = 0
                        else:
                            total = i * (num+1)
                    else:
                        total = 0
                else:
                    if i !="완전잠식":
                        if math.isnan(i) == True:
                            total = total 
                        else:
                            total = total + i * (num+1)
                    else:
                        total = total    
                        
            srim_df.loc[stock_code,'ROE'] = total/6



        else:
            pass



        # 발행주식수, 최근종가 추출
        df_shares = pd.read_html(r.text,match = '종가' )  
        df_shares = df_shares[0].copy()
        s = df_shares.iloc[-1,1]
        s = s.split('/')
        s1 = s[0].replace(',','') #보통주
        s2 = s[1].replace(',','') #우선주
        price = df_shares.iloc[0,1].split('/')[0].replace(',','') #최근종가

        srim_df.loc[stock_code,'발행주식수_보통주'] = int(s1)
        srim_df.loc[stock_code,'발행주식수_우선주'] = int(s2) 
        srim_df.loc[stock_code,'최근종가'] = int(price)  
        
        
    except ValueError: 
        print("ValueError : {}".format(stock_code))
        continue
    except KeyError:   
        print("KeyError : {}".format(stock_code))
        continue
    except IndexError:   
        print("IndexError : {}".format(stock_code))
        continue  
        
        
    
    
srim_df
# 기대수익률 
url = 'http://kisrating.com/ratingsStatistics/statics_spread.do#'
r = requests.get(url)
df = pd.read_html(r.text)  
df = df[0]
rate = df.loc[df['구분'] == 'BBB-','5년'].apply(pd.to_numeric)
rate = rate.values
rate = rate[0]

srim_df['기대수익률'] = rate
srim_df
# srim계산
srim_df['S-RIM'] = srim_df['지배주주지분'] + (srim_df['지배주주지분'] *(srim_df['ROE'] - srim_df['기대수익률'] ))/srim_df['기대수익률'] 
srim_df['S-RIM_-10%'] = srim_df['지배주주지분']  + (srim_df['지배주주지분'] *(srim_df['ROE'] - srim_df['기대수익률']))*0.9/(1+srim_df['기대수익률']-0.9)
srim_df['S-RIM_-20%'] = srim_df['지배주주지분']  + (srim_df['지배주주지분'] *(srim_df['ROE'] - srim_df['기대수익률']))*0.8/(1+srim_df['기대수익률']-0.8)

# 목표주가계산
srim_df['매도주가'] = srim_df['S-RIM'] / ( srim_df['발행주식수_보통주'] +  srim_df['발행주식수_우선주']) * 100000000
srim_df['적정주가'] = srim_df['S-RIM_-10%'] / ( srim_df['발행주식수_보통주'] +  srim_df['발행주식수_우선주']) * 100000000
srim_df['매수주가'] = srim_df['S-RIM_-20%'] / ( srim_df['발행주식수_보통주'] +  srim_df['발행주식수_우선주']) * 100000000

print(srim_df)
# 초과수익여부
srim_df['초과수익'] = srim_df['ROE'] > srim_df['기대수익률']

# 매수판단
srim_df['매수판단'] = srim_df['매수주가'] > srim_df['최근종가']

# 매수판단
srim_df.loc[(srim_df['초과수익']==True)&(srim_df['매수판단']==True),'매수여부'] = '매수'
srim_df.loc[(srim_df['초과수익']!=True)|(srim_df['매수판단']!=True),'매수여부'] = '-'

# 매수시 수익률
srim_df['1차 기대수익률'] = (srim_df['적정주가']/srim_df['최근종가'] - 1) * 100
srim_df['2차 기대수익률'] = (srim_df['매도주가']/srim_df['최근종가'] - 1) * 100

print(srim_df)
srim_df.to_excel('d:/finance/srim_df.xlsx')
srim.to_excel('d:/finance/srim.xlsx')
