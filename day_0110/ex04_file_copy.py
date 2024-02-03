# ----------------------------------------------------------------------------
# 파일을 하나 선택 후 복사본 파일 생성하기
# - 예) message.txt ====> message_copy.txt
# ----------------------------------------------------------------------------
'''
⚠️ERROR 발생!!!!!!!!!!!!!!!!!!! 없는 폴더를 첨에 변수로 지정해서 그런가??

filename = 'message_copy.txt'
existfile = 'message.txt'

# 1 파일 열었음
file_new = open(filename,mode = 'w', encoding = 'utf - 8')
file_original = open(existfile, mode='a', encoding = 'utf - 8')

# 2 기존 파일에서 읽어옴

datas = existfile.readlines()

# 3 읽어온 걸 써준다.
for d in datas:
    filename.write(d)

# 4 close
filename.close()
existfile.close()
'''




# 강사님 방식 ----------------------------------
filename = 'message.txt'

# 방법1
# 원본 파일에 내용 읽은 후 저장
with open(filename, mode = 'r', encoding = 'utf8') as f:
    data = f.read()

# 복사본 파일에 내용 쓰기
with open('message_copy.txt', mode = 'w', encoding = 'utf8') as f:
    f.write(data)
# - 여기서는 둘다 f로 해도 됨


# 방법2
# 원본 파일에 내용 읽은 후 새 파일에 바로 저장
with open(filename, mode = 'r', encoding = 'utf8') as of:
    with open('message_copy.txt', mode = 'w', encoding = 'utf8') as nf:
        nf.write(of.read())
# - 여기서는 파일의 이를 다르게 설정해야함
