#클래스 생성
class person: # person을 정의하는 거임.
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    # #1. 생성자 추가
    # def __init__(self):
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'

    def __init__(self, name = '홍길동',  height = 170, gender = 'male') -> None: 
            self.name = name
            self.height = height
            self.gender = gender

            

    def walk(self):
        print(f'{self.name}이 걷습니다')

    def run(self,option): 
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이 빨리 뜁니다!!')
        else:
            print('천천히 뜁니다!!')

    def stop(self):
        print(f'{self.name}이 멈춥니다') 

    #생성자와 매직매서드 (펑션)__str__
    def __str__(self):
         return f'출력 / 이름은 {self.name} 입니다.'

soojin = person() #객체를 생성 객체는 변수와 함수의 집합입니다.person을 만들어라 동사임 함수랑 똑같음 함수를 만들어라.
#soojin.name = '수진'
#soojin.height = '168'
#soojin.gender = 'female'
#soojin.blood_type = 'RH+AB'

print(f'{soojin.name}의 혈액형은 {soojin.blood_type}입니다.')

soojin.run('Fast')


# 1. 초기화 후 객체생성
hong = person()
hong.run('Slow')
print(hong)

print('====================')
#파라미터를 받는 생성자 실행
ashely = person('애슐리', 165, 'female') #
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)
