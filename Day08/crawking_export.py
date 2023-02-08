# %% [markdown]
# ## 웹 크롤링
# 
# ### 인터넷 접속 라이브러리 추가

# %%
from urllib.request import urlopen, Request

#도시별 날씨 검색함수
def get_weather(city):
    # 기상청 홈페이지 도시별 날씨
    url = 'https://www.weather.go.kr/w/obs-climate/land/city-obs.do'
    page =  urlopen(url=url)

    text= page.read().decode('utf-8')
    text=text[text.find(f'>{city}</a'):]
    # 기온 가져오기
    for i in range(7):
        text= text[text.find('<td>')+1:]
        
    start=3
    end=text.find('</td>')
    current_temp= text[start:end]
    print(f'{city}의 현재기온은 {current_temp}˚C 입니다')

    #습도 가져오기
    for i in range(3):
        text= text[text.find('<td>')+1:]
        
    start=3
    end=text.find('</td>')
    current_temp= text[start:end]
    print(f'{city}의 현재 습도는 {current_temp}% 입니다.')


get_weather('부산')


