# 입력 시(hour) 분(minute)이 콜론(':') 으로 구분되어 한 줄로 입력
# "시:분" 형태로 입력된다.
hour,minute=input().split(':')
print(hour,minute,sep=':')