import pandas as pd
import numpy as np
import seaborn as sns
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


file_name = "eft_2021-02-04_raw.csv"
df = pd.read_csv(file_name, dtype = {"itemcode":np.object})
print(df["etfTabCode"].value_counts().sort_index())
print(df[df["etfTabCode"] == 1])

eftcode = """전체
국내 시장지수
국내 업종/테마
국내 파생
해외 주식
원자재
기타
"""
print(eftcode)
etf_tab_name = eftcode.split("\n")

def find_eft_tab_name(no):
    return etf_tab_name[no]

find_eft_tab_name(2)

df["etfTabName"] = df["etfTabCode"].map(lambda x : etf_tab_name[x])
print(df.loc[df["etfTabCode"] == 5, ["itemname", "etfTabName"]])

"""종목명
현재가
전일비
등락률
NAV
3개월수익률
거래량
거래대금(백만)
시가총액(억)
"""

cols = df.columns.tolist()
print(cols)

col_name = """종목코드
탭코드
종목명
현재가
등락구분
전일비
등락률
순자산가치(NAV)
3개월수익률
거래량
거래대금(백만)
시가총액(억)
유형"""
col_name = col_name.split("\n")
print(dict(zip(cols, col_name)))
df.columns = col_name
print(df.describe(include=np.object))
print(df.nunique())

#df["유형"].value_counts().plot.barh()

sns.countplot(data=df, y="유형", hue="인버스")
#print(df["유형"].value_counts(normalize=True)* 100)

plt.show()



