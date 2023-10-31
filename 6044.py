# 입력: 정수 2개가 공백을 두고 입력된다.
# 출력: 첫 번째 줄에 합, 두 번째 줄에 차, 세 번째 줄에 곱, 네 번째 줄에 몫, 다섯 번째 줄에 나머지

a,b=input().split()
a,b=int(a),int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b,".2f"))