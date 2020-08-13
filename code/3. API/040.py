# 구글 검색 트렌트 (추천 검색어)
from pytrends.request import TrendReq
import matplotlib.pyplot as plt 
import os 

# Google Trend 접속
trend_obj = TrendReq()

# 검색 keyword에 대한 추천 검색어 확인
keyword = "WTO"
suggested_keywords = trend_obj.suggestions(keyword)
print(suggested_keywords)
print("\n")

new_keyword = suggested_keywords[2]['title']
print(new_keyword)
print("\n")

# 검색을 위한 데이터 탑재
period = "now 7-d" # 검색기간: 최근 7일
trend_obj.build_payload(kw_list=[new_keyword], timeframe=period)

# 상위 30개 지역을 선택
trend_df = trend_obj.interest_by_region()
print(trend_df.head())
trend_top30 = trend_df.sort_values(by=new_keyword, ascending=False).head(30)
print(trend_top30.head())
print("\n")

# 그래프 출력
plt.style.use("ggplot")
plt.figure(figsize=(15,15))
trend_top30[new_keyword].plot(kind='bar')
plt.title("Google Trends by Resion", size=15)
plt.legend(labels=[new_keyword], loc='upper right')

# 그래프 파일 저장
cwd = os.getcwd()
output_filepath = os.path.join(cwd, "code\\3. API\\output", "google_trend_by_region_%s.png" % new_keyword)

plt.savefig(output_filepath, dpi=300)
plt.show()