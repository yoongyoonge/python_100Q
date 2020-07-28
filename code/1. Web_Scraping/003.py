# 대부분의 사이트들이 웹 크롤링 로봇의 접근 권한에 대하여 설정하고 있음
# 웹 페이지에 접그하기 전에 반드시 로봇 배제 표준을 확인하고 가이드라인을 준수할 필요가 있음

import requests

urls=["https://www.naver.com/", "https://www.python.org/"]
filename="robots.txt"

for url in urls:
    file_path = url + filename
    print(file_path)
    
    resp = requests.get(file_path)

    print(resp.text) #text 속성은 HTML 소스를 저장하고 있음
    print("end")
    print("\n")
    