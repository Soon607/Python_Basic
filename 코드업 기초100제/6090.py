# 입력
# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가
# 공백을 두고 입력된다.(a, m, d는 -50 ~ +50, n은 10이하의 자연수)

# 출력
# n번째 수를 출력한다.

a,m,d,n=map(int,input().split())

s=a

for i in range(2,n+1):
    s=(s*m)+d
    
print(s)