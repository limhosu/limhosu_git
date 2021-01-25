# financedatareader로 개별 종목의 일별 시세 수집
import pandas as pd
import FinanceDataReader as fdr
import seaborn as sns
import numpy as np
def get_font_family():
    """
    시스템 환경에 따른 기본 폰트명을 반환하는 함수
    """
    import platform
    system_name = platform.system()
    # colab 사용자는 system_name이 'Linux'로 확인

    if system_name == "Darwin" :
        font_family = "AppleGothic"
    elif system_name == "Windows":
        font_family = "Malgun Gothic"
    else:
        # Linux
        # colab에서는 runtime을 <꼭> 재시작 해야합니다.
        # 런타임을 재시작 하지 않고 폰트 설치를 하면 기본 설정 폰트가 로드되어 한글이 깨집니다.
        import matplotlib.font_manager as fm

        fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
        font = fm.FontProperties(fname=fontpath, size=9)
        fm._rebuild()
        font_family = "NanumBarunGothic"
    return font_family

get_font_family()
import matplotlib.pyplot as plt
font_family = get_font_family()
plt.rc("font", family=font_family)
plt.rc("axes", unicode_minus=False)
plt.style.use("ggplot")

df_krx = pd.read_csv("d:/finance/krx.csv")



#def item_code_by_item_name(item_name):
#    """
#    종목명을 방아 종목코드를 찾아 반환하는 함수
#    """
#    item_code_list = df_krx.loc[df_krx["Name"] == item_name, "Symbol"].tolist()
#    if len(item_code_list) > 0:
        
#        item_code = item_code_list[0]
#        return item_code
#    else:
#        return False

#def find_item_list(item_name, year=2020):
#    """
#    종목명을 넘겨주면 일별시세를 반환하는 함수
#    내부에서 종목명으로 종목코드를 반환하는 함수
#    종목의 시세를 수집합니다.
#    """
#    item_code = item_code_by_item_name(item_name)
#    if item_code:
#        df_day = fdr.DataReader(item_code, str(year))
#        print(df_day)
#        return df_day
#    else:
#        return False

#stock_daily = find_item_list("빅히트")
#stock_daily[["Close", "Volume"]].plot(secondary_y="Volume")

#print(df["Close"].plot())

stock_dict = {'삼성전자':'005930',
              'SK하이닉스': '000660',
              '현대차' : '005380',
              '셀트리온' : '068270',
              'LG화학' : '051910',
              'POSCO' : '005490',
              '삼성물산' : '028260',
              'NAVER' : '035420'}

item_list = []
for item_code in stock_dict.values():
    close = fdr.DataReader(item_code, "2020", "2021")["Close"]
    item_list.append(close)
df = pd.concat(item_list, axis=1)
df.columns = stock_dict.keys()
df = df[["삼성전자", "LG화학", "SK하이닉스", "현대차", "셀트리온", "POSCO", "삼성물산", "NAVER"]]
df2 = df[["삼성전자", "LG화학", "SK하이닉스"]]
df_norm = df / df.iloc[0] - 1
print(df_norm)
df_norm.plot()

plt.show()

