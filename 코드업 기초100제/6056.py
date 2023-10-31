# 입력: 2개의 정수가 공백을 두고 입력된다.
# 출력: 두 값의 True/False 값이 서로 다를 경우만 True출력하고 그 외의 경우에는 False출력
a,b=input().split()
c=bool(int(a))
d=bool(int(b))
print((c and (not d)) or ((not c) and d))
