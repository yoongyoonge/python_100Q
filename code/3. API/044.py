# 상장기업 개황정보
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

# dart 전자공시 사이트 apt 인증 키 입력
my_auth_key = "본인의 인증키를 넣으세요"

# 기업개황 정보 접속 url
crp_cd = find_corp_num('005380')
url = "https://opendart.fss.or.kr/api/company.xml?crtfc_key="+my_auth_key+"&corp_code="+crp_cd

# beautifulsoup 으로 api 가 반환하는 xml 해석하여 dataframe으로 정리
xml = requests.get(url)
soup = BeautifulSoup(xml.text, 'html.parser')

corp_code = soup.find('corp_code').text
corp_name = soup.find('corp_name').text
corp_name_eng = soup.find('corp_name_eng').text
stock_name = soup.find('stock_name').text
stock_code = soup.find('stock_code').text
ceo_nm = soup.find('ceo_nm').text
corp_cls = soup.find('corp_cls').text
jurir_no = soup.find('jurir_no').text
bizr_no = soup.find('bizr_no').text
adres = soup.find('adres').text
hm_url = soup.find('hm_url').text
ir_url = soup.find('ir_url').text
phn_no = soup.find('phn_no').text
fax_no = soup.find('fax_no').text
induty_code = soup.find('induty_code').text
est_dt = soup.find('est_dt').text
acc_mt = soup.find('acc_mt').text


company_info = {
    'corp_code':corp_code
    , 'corp_name':corp_name
    , 'corp_name_eng':corp_name_eng
    , 'stock_name':stock_name
    , 'stock_code':stock_code
    , 'ceo_nm':ceo_nm
    , 'corp_cls':corp_cls
    , 'jurir_no':jurir_no
    , 'bizr_no':bizr_no
    , 'adres':adres
    , 'hm_url':hm_url
    , 'phn_no':phn_no
    , 'fax_no':fax_no
    , 'induty_code':induty_code
    , 'est_dt':est_dt
    , 'acc_mt':acc_mt
}

print(company_info)