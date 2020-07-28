import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, "html.parser")

#img 태그 부분을 찾아 저장
target_img = soup.find(name="img", attrs={"alt":"Seoul-Metro-2004-20070722.jpg"})
print("HTMP 요소: ", target_img)
print("\n")

#속성이 갖는 값을 추출
#이미지 파일의 저장 경로 URL을 따로 추출하여 변수에 저장
target_img_src = target_img.get("src")
print("이미지 파일 경로: ", target_img_src)
print("\n")

#파일경로를 보완하고 get함수를 적용하여 응답 객체를 target_img_resp에 저장
target_img_resp = requests.get("http:" + target_img_src)
out_file_path = "./code/1. Web_Scraping/output/download_image.jpg"



# 파일 저장 시 상대경로로 표현하기 위한 참고 자료
#import os
#print (os.getcwd()) #현재 디렉토리의
#print (os.path.realpath(file))#파일
#print (os.path.dirname(os.path.realpath(file)) )#파일이 위치한 디렉토리



# requests 응답 객체의 content 속성에는 이미지 파일이 바이너리 형태로 저장되어있음
with open(out_file_path, 'wb') as out_file:
    out_file.write(target_img_resp.content)
    print("이미지 파일로 저장하였습니다.")
