# 입력: 2개의 정수가 공백을 두고 입력된다
# 출력: 둘다 True일 경우에만 True를 출력하고 그 외에는 False를 출력한다.
a,b=input().split()
print(bool(int(a)) and bool(int(b)))