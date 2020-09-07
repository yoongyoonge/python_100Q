# 전체 상장기업의 지분공시자료 검색 및 다운로드

# 본 코드
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import datetime as dt

# dart 전자공시 사이트 apt 인증 키 입력
my_auth_key = "9e095364707184ea6fbb0ff51fb89c4bb339fe4a"

# 검색 기간 설정하기
now = dt.datetime.now()
search_period = dt.timedelta(days=5)
now_date = now.strftime('%Y%m%d')
bgn_de = (now-search_period).strftime('%Y%m%d')
page_count = 10


# dart 상세정보 접속 url
pblntf_detail_ty_list = [
    "D001", # 주식 등의 대량보유 상황보고서
    "D002", # 임원, 주요 주주 특정증권 등 소유 상황보고서
    "D003", # 의결권 대리 행사 권유
    "D004", # 공개 매수
]

pblntf_detail_ty_urls = []

for pblntf_detail_ty in pblntf_detail_ty_list:
    url = "https://opendart.fss.or.kr/api/list.xml?crtfc_key="+my_auth_key+"&page_count="+str(page_count)+"&bgn_de="+bgn_de+"&pblntf_detail_ty="+pblntf_detail_ty
    pblntf_detail_ty_urls.append(url)

# BeautifulSoup으로 api가 반환하는 xml 해석하여 dataframe으로 정리

sum_items = []

for url in pblntf_detail_ty_urls:
    xml = requests.get(pblntf_detail_ty_urls[1])
    soup = BeautifulSoup(xml.text, 'html.parser')
    items = soup.find_all('list')
    sum_items += items


print(len(sum_items))
print("\n")

search_result = pd.DataFrame()

for item in sum_items:
    temp_dataframe = pd.DataFrame(([[item.corp_cls.text, item.corp_name.text, item.corp_code.text,
                                    item.stock_code.text, item.report_nm.text, item.rcept_no.text,
                                    item.rcept_no.text, item.flr_nm.text, item.rcept_dt.text, item.rm.text]]),
                                    columns=["corp_cls", "corp_name", "corp_code", "stock_code", "report_nm", "rcept_no", "rcept_no", "flr_nm", "rcept_dt", "rm"])
    
    search_result = pd.concat([search_result, temp_dataframe])

print(search_result.head())