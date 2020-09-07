# 회사의 최근 3개월 공시자료 검색 및 다운로드

import xml.etree.ElementTree as ET

tree = ET.parse('./corp_num/CORPCODE.xml')
root = tree.getroot()

# stock_code로 회사 고유번호 찾기
def find_corp_num(find_stock_num):
    for country in root.iter("list"):
        if country.findtext("stock_code") == find_stock_num:
            return country.findtext("corp_code")


# 본 코드
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import datetime as dt

# dart 전자공시 사이트 apt 인증 키 입력
my_auth_key = "본인의 인증키를 넣으세요."

# 검색 기간 설정하기
now = dt.datetime.now()
search_period = dt.timedelta(days=30)
now_date = now.strftime('%Y%m%d')
bgn_de = (now-search_period).strftime('%Y%m%d')
page_count = 10

# dart 상세정보 접속 url
corp_code = find_corp_num('005380')
url = "https://opendart.fss.or.kr/api/list.xml?crtfc_key="+my_auth_key+"&corp_code="+corp_code+"&page_count="+str(page_count)+"&bgn_de="+bgn_de

# beautifulsoup 으로 api 가 반환하는 xml 해석하여 dataframe으로 정리
xml = requests.get(url)
soup = BeautifulSoup(xml.text, 'html.parser')
print(str(soup)[:500])
print("\n")

search_result = pd.DataFrame()
items = soup.find_all("list")
print(len(items))
print("\n")

for item in items:
    temp_dataframe = pd.DataFrame(([[item.corp_cls.text, item.corp_name.text, item.corp_code.text,
                                    item.stock_code.text, item.report_nm.text, item.rcept_no.text,
                                    item.rcept_no.text, item.flr_nm.text, item.rcept_dt.text, item.rm.text]]),
                                    columns=["corp_cls", "corp_name", "corp_code", "stock_code", "report_nm", "rcept_no", "rcept_no", "flr_nm", "rcept_dt", "rm"])
    search_result = pd.concat([search_result, temp_dataframe])


print(search_result)