#Car 클래스를 상속한 제네시스 클래스
from code37_car import Car

class Genesis(Car):
    def __init__(self, name, color,
                  plate_number, product_year) -> None:
        super().__init__()

        self.__name = name
        self.__color = color
        self.__plate_number = plate_number
        self.__product_year = product_year
        print(f'{self.__name}인스턴스 생성!')

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def run(self):
        return f'{self.__name}가 달립니다'
    
    def stop(self):
        return f'{self.__name}가 멈춥니다'


gv80 = Genesis('팔공이','black', '66오 1004', 2022)
gv80.set_name('팔공이')
print(f'이 차의 이름은 {gv80.get_name()}입니다')
print(gv80.run())
print(gv80.stop())
