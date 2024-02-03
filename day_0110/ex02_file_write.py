# ---------------------------------------------------------------------------
# 파일 입출력 => 출력 즉, 쓰기 (write)
# - 사용 내장 함수 : open(file, mode = 'w', encoding = '지정')
# ---------------------------------------------------------------------------
filename = 'mydata.txt'
existfile = 'messsage.txt'

# (1) open => 쓰기(w) 모드의 경우 파일이 없으면 생성, 있으면 모든 내용 지움
# file = open(filename, mode = 'w', encoding = 'utf-8')
# - 기본값은 읽는거라 모드를 반드시 설정해야 쓰기 가능
# - 이걸 실행시키면 파일이 새로 생긴다.

# (1_2) open => 쓰기(a) 모드의 경우 파일이 없으면 생성, 있으면 제일 마지막에 추가
file = open(filename, mode='a', encoding = 'utf-8')
# -  여기서 a는 append


# (2) write
file.write("123456\n")  # - 이걸 실행시키면 생성된 파일안에 작성
file.write("""ha ha ha
aaaaa
11111""")
# - 근데 윗줄에것이 지우고 만들어지는게 아닌가? ㄴㄴ 그거는 모드와 관련있는 기능이다!

file.writelines(['a\n', 'b\n', 'c\n'])
# - 이르케 하기보다는 리스트 컴프리헨션으로 \n 추가해주면 간단하게 가능

# (3) close
file.close()