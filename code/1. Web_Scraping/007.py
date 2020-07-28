import requests, re #정규식 표현을 사용하기 위해 re 모듈을 불러옴
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, "html.parser")

links = soup.find_all("a")
print("하이퍼링크의 개수: ", len(links)) #원소의 개수 확인, 여기에서는 a태그의 개수를 뜻함
print("\n")
print("첫 3개의 원소: ", links[:3])
print("\n")

wiki_links = soup.find_all(name="a", href=re.compile("/wiki/"), limit=3) #/wiki/ 문자열이 포함된 태그를 3개만 찾음
print("/wiki 문자열이 포함된 하이퍼링크: ", wiki_links)
print("\n")

external_links = soup.find_all(name="a", attrs={"class":"external text"}, limit=3) #class 속성값이 external text인것을 3개만 찾음
print("class 속성으로 추출한 하이퍼링크", external_links)