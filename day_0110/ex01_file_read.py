# -------------------------------------------------------------------------------
# 파일 입출력 => 출력 즉, 읽기(read)
# - 사용 내장 함수 : open(file, mode = 'rt[기본값]', encoding = '시스템기본기')
# - encoding 설정 : 파일에 적용된 인코딩을 설정해야함!
# -------------------------------------------------------------------------------
# (1) open
file = open('message.txt', encoding ='utf8')
print(f'file = {type(file)}, {file}')


# (2) IO => read() : 파일 안에 모든 내용 다 읽어오기
# fData = file.read()     #파일을 읽어오는 메소드
# print(f'fData = {type(fData)}, {fData}')


# (2_1) IO => read(n): 지정된 숫자만큼 문자를 파일에서 읽어옴
fData = file.read(5) # 지정된 숫자 만큼 문자 읽기
# - 5바이트만 나온다.
# - 만약 윗줄을 주석처리하지 않으면 이 부분은 나오지 않음. 왜냐 파일 내용의 가장 끝 커서로 가기 때문에 더 읽은게 없음
# print(f'fData = {type(fData)}, {fData}')
#
# fData = file.read(5)
# print(f'fData = {type(fData)}, {fData}')


# (2_2) IO => readline(): '\n' 기준으로 한 줄 읽어오기
# datas = []
# while True:
#     fline = file.readline()
#     if not fline: break           # 멈추기 위해 글내용이 없으면 break 걸었다.
#     print(f'fline => {type(fline)}  {fline}', end='')  #원본파일에서 줄바꿈시에는 공백이더라도 \n이 포함되어있다.
#     datas.append(fline)
# print(datas)

# (2_3) IO => readline(): '\n' 기준으로 한 줄씩 읽은 것을 리스트에 담아서 반환
datas = file.readlines()
print(datas)


# (3) close
file.close()     #열었으니 닫아준다.

