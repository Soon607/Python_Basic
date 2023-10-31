# 입력: 두개의 정수가 공백을 두고 입력된다.
# 출력: 두 값의 True/False값이 서로 같을 경우만 True출력하고 그 외의 경우에는 False출력
a,b=input().split()
c=bool(int(a))
d=bool(int(b))
print(c==d)