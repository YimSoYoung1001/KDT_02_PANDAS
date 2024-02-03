# -----------------------------------------------------------------------------
# 자동차 관리 프로그램 만들기
# - 엔진, 연료, 브랜드, 색상, 번호
# - 전진, 후진, 자회전, 우회전, 정지
# -----------------------------------------------------------------------------
# engine = '휘발유엔진'
# food = '휘발유'
# maker = '현대'
# color = '흰색'
# number = '111가 1111'
#
# engine2 = '휘발유엔진'
# food2 = '휘발유'
# maker2 = '현대'
# color2 = '흰색'
# number2 = '111가 2222'
#
# engine3 = '휘발유엔진'
# food3 = '휘발유'
# maker3 = '현대'
# color3 = '흰색'
# number3 = '111가 3333'
#
# def go(number) : print(f'{number} 자동차가 전진')
# def back(number) : print(f'{number} 자동차가 후진')
# def left_go(number) : print(f'{number} 자동차가 좌회전')
# def right_go(number) : print(f'{number} 자동차가 우회전')
# def stop(number) : print(f'{number} 자동차가 정지')
#
# carDict = {'111가 1111': {engine3:'휘발유엔진', food3:'휘발유', maker3:'현대', 'autodrive':False},
#            '111가 2222': {engine3:'휘발유엔진', food3:'휘발유', maker3:'기아', 'autodrive':False},
#            '111가 3333': {engine3:'휘발유엔진', food3:'경유', maker3:'현대', 'autodrive':True}}
#
# # 자동차 관리 -------------------------------------------------------------------
#
# for k, v in carDict.items():
#     print(f'판매 차량 [{k}]')
#     for subK, subV in v.items():
#         print(f'- {subK} : [{subV}]')



# --------------------------------------------------------------------------------------------
# 자동차 클래스
# - 역할 : 자동차 관련 데이터, 기능을 모두 저장 관리 클래스
# - 문법
#   class 클래스명 :
#   <---> 코드
# --------------------------------------------------------------------------------------------
class Car:
    maker = '현대'

    # 클래스 생성시 필수로 사용되는 메서드
    # 힙 메모리에 속성들의 값을 저장해주는 역할
    def __init__(self, engine_, food_, color_, number_ ):
        print('__init__')
        # 자동차 클래스 가지는 속성 메모리 힙에 저장
        # - self 라는 주소에 가서 저장해라!
        self.engine = engine_   # - 값을 저장하고 그 주소를 engine이라는 주소에 저장해라
        self.color = color_
        self.number = number_

    # 자동차 기능 => 함수 형식
    def go(self):
        print(f'{self.number} 자동차 전진')
    def back(self):
        print(f'{self.number} 자동차 후진')

    def stop(self):
        print(f'{self.number} 자동차 정지')

# 클래스로 자동차 객체 생성 ---------------------------------------------------------------------

myCar = Car('휘발유엔진','현대','휘발유','흰색','111가1111')
myCar2 = Car('휘발유엔진','현대','휘발유','핑크색','777가7777')

'''
data 타입
- int, float, list 등등이 있는데 여기에 사용자 정의 타입으로 car가 생긴것!
'''

myCar.go()
