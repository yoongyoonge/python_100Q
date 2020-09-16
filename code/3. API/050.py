# 구글 지오코딩 / folium 맵 만들기

import folium

# 서울 지도 만들기
seoul_map1 = folium.Map(location=[37.55, 126.98], zoo_start=12)

seoul_map2 = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain', zoo_start=9)

seoul_map3 = folium.Map(location=[37.55, 126.98], tiles='Stamen Toner', zoo_start=15)

# 지도를 HTML 파일로 저장하기
seoul_map1.save('./code/3. API/output/seoul1.html')
seoul_map2.save('./code/3. API/output/seoul2.html')
seoul_map3.save('./code/3. API/output/seoul3.html')