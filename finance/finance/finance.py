# financedatareader로 거래소 전체 종목 리스트 가져오기
import pandas as pd
import FinanceDataReader as fdr
import seaborn as sns
import numpy as np

df_kospi = fdr.StockListing("KOSPI")
df_kospi.to_csv("d:/finance/kospi.csv", index=False)
df = pd.read_csv("d:/finance/kospi.csv")
df["ListingDate"]=pd.to_datetime(df["ListingDate"])

df["ListingYear"]=df["ListingDate"].dt.year
print(df[["ListingDate", "ListingYear"]])
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



# plt.show()

# plt.figure(figsize=(15, 4))
# sns.lineplot(data=df_year_market, x="ListingYear", y="count", hue="Market", ci=None)
# plt.show()
# df = df[df["ListingYear"] < 1970]
#df_sr = pd.crosstab(df["Sector"], df["Region"])

#print(df_sr.loc["소프트웨어 개발 및 공급업"])
