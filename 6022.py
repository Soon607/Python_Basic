# 입력: 6자리 숫자로 이루어진 YYMMDD이 입력된다.
# 출력: YY MM DD을 공백으로 구분해 한 줄로 출력된다.
date=input()
print(date[0:2],date[2:4],date[4:],sep=" ")