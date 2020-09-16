# 구글 지오코딩 / 지리 정보(위도, 경도) 가져오기

# 구글 지오코딩 서비스 : 주소 -> 위도와 경도 좌표 정보

import googlemaps

my_key = "본인의 인증키를 입력하세요"

# 구글맵스 객체 생성하기
maps = googlemaps.Client(key=my_key)

# 장소명 또는 주소
place = "교보문고 광화문점"

# 지오코딩 api 결과값 호출하여 geo_location 변수에 저장
geo_location = maps.geocode(place)[0].get('geometry')
print(geo_location)
print("\n")

lat = geo_location['location']['lat']
lng = geo_location['location']['lng']

print("위도:", lat)
print("경도:", lng)