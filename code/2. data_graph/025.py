import pandas as pd
import matplotlib.pyplot as plt

# 예제 017의 CSV 파일을 다시 활용하여, 데이터프레임으로 변환
df = pd.read_csv('./code/data/bok_statistics_CD.csv', header=None)
print(df.head())
print('\n')

df.columns = ['year', 'CD_rate', 'change'] # 열 이름 변경
df.set_index('year', inplace=True) # year 열을 행 인덱스로 설정
print(df.head())
df.to_csv('./code/data/bok_statistics_CD_2.csv')
print('\n')

# 선 그래프 그리기, plot은 라인을 따로 영역을 지정하여 부분 실행
df.plot() 
plt.show()


df['CD_rate'].plot()
plt.show()


df['change'].plot()
plt.show()