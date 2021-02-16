# 네이버에서 투자자별 데이터 가져오기(오늘코드)
import requests as rq
import pandas as pd
import os
from os import path
item_code = "005490"
item_name = "포스코"


def get_day_list(item_code, page_no):
    """
    일자별 시세를 페이지별로 가져오기
    """
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

    url = f'https://finance.naver.com/item/frgn.nhn?code={item_code}&page={page_no}'
    r = rq.get(url, headers={"user-agent": user_agent}) # headers지정안하면 뒤에 error가 나네요
    tb = r.content.decode('euc-kr')
    #naver encoding이 euc-kr로 되어있어서 cp949나 utf-8은 안되네요.
    #table = pd.read_html(tb) 이렇게 실행하면 list형식으로 반환되어 사용어렵네요.
    table = pd.read_html(tb, header = 0)[2] #dataFrame
    df_day = table.dropna()
    return df_day
    
page_no = 1
get_day_list(item_code, page_no)
import time
page_no = 1
item_list = []

while True:
    df_day = get_day_list(item_code, page_no)
    item_list.append(df_day)

    page_no = page_no + 1
    time.sleep(0.1)
    if len(df_day) < 20:
        break

df = pd.concat(item_list)

df = df.drop_duplicates()
date = df.iloc[1]['날짜']
file_name = f"{item_name}_{item_code}_{date}.csv"
folder = r'd:/finance/{0}'.format(item_name)
if not path.isdir(folder):
    os.mkdir(folder)
df.to_csv('{0}/{1}'.format(folder, file_name), index=False)
#pd.read_csv('d:/finance/{1}'.format(file_name))



