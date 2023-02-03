#외부 패키지를 사용
import requests

res = requests.get('http://www.naver.com')
print(res.status_code)

print(res.content)
print('=============')
print()