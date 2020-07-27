# 002. 웹 페이지 소스코드 확인하기
# 학습 내용 : 웹 서버가 보내주는 응답 객체의 여러 속성 중에서 HTML 소스코드를 구분할 수 있다.
# 힌트 내용 : 응답 객체의 text 속성을 print() 함수로 출력해본다.

import requests

url = "https://www.python.org/"
resp = requests.get(url) # 웹 사이트에 GET 요청을 보내고 응답한 내용을 resp에 저장

html = resp.text # 웹 서버의 응답 객체는 headers, cookies, text 등 여러 속성을 가짐, 소스코드 확인 방법
print(html)