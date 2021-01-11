# xperp 데이터 가져와서 동,호별로 만들기
import pandas as pd
data = pd.read_excel('d:/2020전기검침/202011테스트.xlsx') #0
data = data.dropna(how='all', axis=1) #1
data = data.drop(columns=['Unnamed: 10','Unnamed: 14','Unnamed: 18']) #2
start_rows = data.loc[data.iloc[:,1]=='호'].index #3
cols = data.loc[start_rows[0]].str.replace('\s','') #4
df = pd.DataFrame(columns=cols) #5
for row in start_rows[:-1] : #6
    df = pd.concat([df, pd.DataFrame(data.loc[row+1:row+43].values, columns = cols)]) #7
df['동'] = df['동'].fillna(method='ffill') #8
df.to_excel('d:/2020전기검침/202011테스트_복사본.xlsx') #9

