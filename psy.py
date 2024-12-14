import folium
import pandas as pd

# 1. 내전 중인 국가 리스트 (미국과 한국은 제외, 추가된 국가 포함)
conflict_countries = ['Somalia', 'South Sudan', 'Sudan', 'Ethiopia', 'Israel', 'Libya', 'Eritrea', 'Central African Republic', 'Mozambique']

# 2. 국가명과 해당 국가에 대한 정보 (사진 파일 경로 포함)
country_info = {
    'Somalia': {
        'info': '''
            1991년 소말리아의 바레 군사 정권이 붕괴된 이후, 중앙 정부가 무너지고 소말리아는 무정부 상태로 빠져
            군벌들 간의 권력 다툼과 지역적 충돌이 심화되었습니다. 내전으로 인해 병원 건물이 파괴되고, 의료 인력들이
            해외로 이주해 남아있는 인력은 매우 부족해졌습니다. 특히 남부 지역은 더욱 심각한 의료적 어려움을 겪고
            있으며, 소말리아는 현재까지도 정치적 불안정과 지속적인 폭력을 겪고 있습니다.
        ''',
        'image': 'file:///C:/Users/채민성/Documents/somalia.jpg'  # 소말리아 이미지 경로 수정
    },
    'South Sudan': {
        'info': 'South Sudan has been affected by civil war since its independence.',
        'image': 'https://example.com/south_sudan_image.jpg'  # 여기에 실제 이미지 URL을 넣으세요.
    },
    'Sudan': {
        'info': 'Sudan is currently undergoing a political and humanitarian crisis.',
        'image': 'https://example.com/sudan_image.jpg'  # 여기에 실제 이미지 URL을 넣으세요.
    },
    'Ethiopia': {
        'info': 'Ethiopia is dealing with internal conflict, particularly in the Tigray region.',
        'image': 'https://example.com/ethiopia_image.jpg'  # 여기에 실제 이미지 URL을 넣으세요.
    },
    'Israel': {
        'info': 'Israel is involved in ongoing political and military conflicts.',
        'image': 'https://example.com/israel_image.jpg'  # 여기에 실제 이미지 URL을 넣으세요.
    },
    'Libya': {
        'info': 'Libya is in a state of civil conflict and political instability.',
        'image': 'https://example.com/libya_image.jpg'  # 여기에 실제 이미지 URL을 넣으세요.
    },
    'Eritrea': {
        'info': 'Eritrea faces political and military conflict with neighboring countries.',
        'image': 'https://example.com/eritrea_image.jpg'  # 여기에 실제 이미지 URL을 넣으세요.
    },
    'Central African Republic': {
        'info': 'The Central African Republic is in the midst of ongoing civil war.',
        'image': 'https://example.com/central_african_republic_image.jpg'  # 여기에 실제 이미지 URL을 넣으세요.
    },
    'Mozambique': {
        'info': 'Mozambique faces conflict, particularly in the northern region.',
        'image': 'https://example.com/mozambique_image.jpg'  # 여기에 실제 이미지 URL을 넣으세요.
    }
}

# 3. Folium 지도 생성 (초기 위치: [20, 0], 줌 레벨: 2)
m = folium.Map(location=[20, 0], zoom_start=2)

# 4. 국가 정보를 담은 DataFrame을 생성하여 각 국가의 좌표를 추가합니다.
# 국가 이름과 좌표 데이터 (위도, 경도) 예시
country_coords = {
    'Somalia': [5.1521, 46.1996],
    'South Sudan': [6.8694, 31.3019],
    'Sudan': [12.8628, 30.8025],
    'Ethiopia': [9.145, 40.4897],
    'Israel': [31.0461, 34.8516],
    'Libya': [26.3351, 17.2283],
    'Eritrea': [15.1794, 39.7823],
    'Central African Republic': [6.6111, 20.9394],
    'Mozambique': [-18.6657, 35.5296]
}

# 5. 내전 중인 나라들을 빨간색으로 표시하고, 팝업에 정보와 이미지를 추가
for country, coords in country_coords.items():
    if country in conflict_countries:
        # 나라 전체를 빨간색으로 칠하기 위해 GeoJSON 스타일을 이용
        folium.Marker(
            location=coords,
            popup=f"""
                <b>{country}</b><br>
                {country_info.get(country, {}).get('info', 'No information available.')}<br>
                <img src="{country_info.get(country, {}).get('image', '')}" width="300" height="200" />
            """,
            icon=folium.Icon(color='red', icon='info-sign')  # 빨간색 아이콘
        ).add_to(m)
    else:
        # 다른 나라들은 기본 색상으로 표시
        folium.Marker(
            location=coords,
            popup=f"""
                <b>{country}</b><br>
                {country_info.get(country, {}).get('info', 'No information available.')}<br>
                <img src="{country_info.get(country, {}).get('image', '')}" width="300" height="200" />
            """,
            icon=folium.Icon(color='blue', icon='info-sign')  # 파란색 아이콘
        ).add_to(m)

# 6. 결과를 HTML 파일로 저장
m.save('world_map_with_conflict_countries_in_red.html')

print("world_map_with_conflict_countries_in_red.html 파일이 생성되었습니다.")
