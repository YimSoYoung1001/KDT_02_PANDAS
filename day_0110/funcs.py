def add(x,y) : return x+y

def div(x,y) : return x/y if y else None

if __name__ == '__main__' :
    print(f'funcs.py => __name__ : {__name__}')
    print(f'add(3, 4) : {add(3,4)}')
    print(f'div(3, 4) : {div(3,4)}')
# - 이르케 조건문으로 가정해주면 import 시켜도 다른 파일에서는 실행 ㄴㄴ
