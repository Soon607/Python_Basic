# 입력: 2개의 정수가 공백을 두고 입력된다.
# 출력: 하나라도 참일 경우 True를 출력하고, 그외의 경우에는 False출력
a,b=input().split()
print(bool(int(a)) or bool(int(b)))
