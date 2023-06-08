# 입력: 정수 2개(a,b)가 공백을 두고 입력된다.
# 출력: a 를 2^b배 만큼 곱한 값을 출력한다.

a,b=input().split()
a,b=int(a),int(b)
print(a*(2**b))


# 답안
# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a<<b)