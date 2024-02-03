# -------------------------------------------------------------------------
# 파일 데이터 접근 관련 메서드
# -------------------------------------------------------------------------
filename = 'message.txt'

with open(filename, mode = 'r', encoding = 'utf8') as f:
    f.seek(5)                          # - 5를 건너서
    print(f.read(10))                  # - 10개를 읽은 후
    print(f'현재위치: {f.tell()}')       # - 위치를 말하라

    print(f.name, f.closed)            # - 중간에 닫겼는지 확인해본다. False 뜸

    f.seek(0)                          # - 처음위치로 가서
    print(f.read(5))                   # - 5개를 읽은 후
    print(f'현재위치: {f.tell()}')       # - 위치를 말하라

print(f.name, f.closed)