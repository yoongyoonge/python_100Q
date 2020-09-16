# 구글 지오코딩 / 지리 정보를 데이터프레임으로 정리하기

# 구글 지오코딩 서비스 : 주소 -> 위도와 경도 좌표 정보

import googlemaps
import pandas as pd

my_key = "본인의 인증키를 입력하세요"

# 구글맵스 객체 생성하기
maps = googlemaps.Client(key=my_key)

lat = []; lng = []

# 장소(또는 주소) 리스트 만들기
place_list = ["서울 종로구 종로 1 교보생명빌딩", "통영시청", "광주비엔날레"]

for i, place in enumerate(place_list):
    try:
        print(i, place)
        geo_location = maps.geocode(place)[0].get('geometry')
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])

    except:
        lat.append(None)
        lng.append(None)

# 데이터프레임으로 변환하기 
df = pd.DataFrame({'장소':place_list, '위도':lat, '경도':lng})
print("\n")
print(df)