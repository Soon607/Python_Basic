# 입력: 두 정수가 공백을 두고 입력된다.
# 출력: 두 정수 중 큰 값을 10 진수로 출력한다.
a,b=input().split()
a,b=int(a),int(b)
c=a if (a>b) else b
print(c)