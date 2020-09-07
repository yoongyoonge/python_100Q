# -*- coding: utf-8 -*-
# DART 접속 및 xml 응답 객체 확인

import requests
from bs4 import BeautifulSoup

#DART 전자공시 사이트 apt 인증키 입력
my_auth_key = "본인의 키를 신청 후 입력"

"""
# 2020.01 월 부로 기업 꽁시 관련 api가 개편되었으므로 다음의 로직을 추각함
# 고유번호 데이터 불러오기
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile

load_corp_code = "https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key="+my_auth_key
with urlopen(load_corp_code) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall('corp_num')
"""

# 위 스크립트를 실행 후 고유번호 정보 파일을 만듦

import xml.etree.ElementTree as ET

tree = ET.parse('./corp_num/CORPCODE.xml')
root = tree.getroot()

# stock_code로 회사 고유번호 찾기
def find_corp_num(find_stock_num):
    for country in root.iter("list"):
        if country.findtext("stock_code") == find_stock_num:
            return country.findtext("corp_code")

# 기업개황 정보 접속 URL
crp_cd = find_corp_num('005380')
url = "https://opendart.fss.or.kr/api/company.xml?crtfc_key="+my_auth_key+"&corp_code="+crp_cd

# BeautifulSoup으로 api 가 반환하는 xml 확인
xml = requests.get(url)
#print(xml.encoding) 
#print(xml.text)
soup = BeautifulSoup(xml.text, 'html.parser')
print(soup)