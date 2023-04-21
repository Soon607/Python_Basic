# 3항 연산자
# 입력된 세 정수 a,b,c 중 가장 작은값을 출력하는 프로그램 작성

a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))

result=(b if c>b else c) if a>b else (a if c>a else c)
print(result)
