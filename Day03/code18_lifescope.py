#라이프 스코프
a = 1

def vartest():
    global a # 전역에 있는 a를 함수(지역)에서 가져다 쓰겠다.
    a = a + 1
    return a

a = vartest() #밖에는 변수 안에는 매개변수
print(a)