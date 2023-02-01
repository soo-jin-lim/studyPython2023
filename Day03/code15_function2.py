#함수
#함수정의 - 이건 실행이 아님
#파라미터 만드는 방법 4가지
#1. 파라미터 O 리턴 O
#2. 파라미터 O 리턴 X
#3. 파라미터 X 리턴 o
#4. 파라미터 X 리턴 X
def add(x, y): # add의 정의
    result = x + y
    print(result)
    

def sub(x, y):
    result = x - y
    print(result)
    

def mul(x, y):
    result = x * y
    print(result)
    

def div(x, y):
    result = x // y
    print(result)
    

def hello():
    print('hello~!!!')

def hello2():
    msg = 'Hello, Hello'
    return msg

# 함수호출
add(1024, 5)
sub(1024, 1000)
mul(512, 2)
div(108, 10)


    