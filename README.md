# studyPython2023
부경대 IoT 파이썬 학습 리포지토리

## day01
1. 기본구성
    - Git/Github 설치 및 연동
    - Visual Studio code 설치 및 연동
    - Python 설치
2. 파이썬 기본
    - 콘솔출력
    - 주석

```python
  # desc : 콘솔출력 - 주석
print('Hello,Python') #콘솔 출력 함수
``` 

## 2일차
1. 파이썬 기본
 - 변수
 - 자료형 
 - 연산자
 - 흐름제어
```python
#문자열 포맷팅
pi = 3.141592
print(f'파이는 {pi}입니다.') #파이는 3.141592입니다.
print(f'파이는 {pi:02f}입니다.') #파이는 3.14입니다.
print(f'파이는 {pi:10.3f}입니다.') #파이는        3.142입니다.

#변수 
val = 1

#불형
print(type(val)) 
print(type(거짓))

print(1 + 1 == 2)

print(거짓 == True)
print(거짓 == False)
print(거짓 is False)

print(bool(1)) # 1 == True
print(bool(0)) # 0 == False
print(bool(2)) # 1이외 값은 True라고 하지마세요```

  ``` 
  ## 3일차
  1. 파이썬 기본
    - 흐름제어
    - if
    - for
    - while
    - 구구단 프로그램
    - 함수

  ## 4일차
1. 파이썬기본
  - 가상환경
  - 객체지향 OOP 
  - 패치,모듈

## 5일차
1. 파이썬 기본
  - 패키지 계속
  - 입출력 다시 처리
  - 예외처리
  
  ## 6일차
  1. 파이썬 기본
    - 콘솔 출력 보충
    - 객체지향 다시
      - 객체 지향 특징
      - 상속, 다중상속

  2. 파이썬 응용
      - 주소록 프로젝트 
      - ![image](https://user-images.githubusercontent.com/123914453/216915868-b2f9f97f-76b8-443c-9db9-a7b71d6db9ca.png)

## 7일차
1. 파이썬 응용
    - 주피터 노트북 사용법
      - 노트북 생성: 파일메뉴> 새파일
    - 리스트 연산 추가
    - 라이브러리 사용법
      - folium (지도 라이브러리)

# 8일차
1. 파이썬 응용
  - 라이브러리 활용법
    - urllib.request
  - 웹 크롤링용 라이브러리
    - 기상청 오늘의 날씨 크롤링
    - 데이터 포털 OpenAPI 크롤링
    - BeautifulSoup 크롤링
  - 자료구조 추가
  - 윈폼 개발(GUI)
  - 응용학습
  

# 9일차
1. 파이썬 응용
  - GUI 개발(pyQt)
  - 자료구조 추가