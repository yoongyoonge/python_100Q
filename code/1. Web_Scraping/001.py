# 001. 웹 서버에 요청하고 응답받기
# 학습 내용 : 웹 서버에 접속하여 웹 페이지 정보를 요청하고 서버로부터 응답 객체를 받는 과정을 이해한다.
# 힌트 내용 : requests 모듈의 get() 함수에 접속하려는 웹 페이지의 주소(URL)를 입력한다.

import requests

url = "https://www.python.org/"
resp = requests.get(url)
print(resp) # 200, 정상 동작

url2 = "https://www.python.org/1"
resp2 = requests.get(url2)
print(resp2) # 404 error, 해당 페이지를 찾을 수 없음