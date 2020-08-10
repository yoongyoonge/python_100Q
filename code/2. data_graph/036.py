# 채색 달력 그래프

import pandas as pd 
import calmap
import matplotlib.pyplot as plt 

pd.set_option('display.max_columns', 20)

# KOSPI 데이터 준비
df = pd.read_excel('./code/data/kospi_2018.xls', parse_dates=['년/월/일'])
print(df.head())
print("\n")

df.columns = ['date', 'price', 'up_down', 'change', 'start', 'high', 'low', 'vol_num', 'vol_amt', 'mkt_cap']
#df.columns = ['년/월/일', '종가', '대비', '등락률(%)', '시가', '고가', '저가', '거래량(천주)', '거래대금(원)', '상장시가총액(원)']

df = df.set_index('date', drop=True)
print(df.head())
print("\n")

# Calendar Map 표현
plt.figure(figsize=(16,8))
calmap.calendarplot(df.change, monthticks=1, daylabels='MTWTFSS', dayticks=[0, 2, 4, 6],
                    cmap='YlGn', linewidth=0.05, fillcolor='grey', fig_kws=dict(figsize=(14,6)),
                    yearlabel_kws=dict(color='black', fontsize=12), subplot_kws=dict(title='2018 KOSPI Price Trend'))

plt.show()
