import os
import code

#자동차 클래스
class Car:
    __number = '307다 8776'

    def get_number(self):
        return self.number
    
    def __init__(sel, number='54라 9538') -> None:
        print('__init__')
        
    def __new__(cls):
        print('__new__')
        return super().__new__(cls)

    def __str__(self) -> str:
        return f'차번호는 {self.__number}'        
    
yourcar = Car('88호 7645')
print(yourcar)
yourcar.__number 
print(yourcar)
print('클래스 내부함수 사용')
yourcar.__number = '54라 9999'    
print(yourcar)
mycar = Car()
print(mycar)
print(f'제 차는요 , 아이오닉이고 번호가 {mycar.get_number()}에요')

mycar.__number = '123거 8745'
print(mycar.get_number)
yourcar.set_number('55오5555')
print(mycar)
print(yourcar)

