# 입력: 30보다 작은 정수 1개가 입력된다.
# 출력: 1 부터 그 수까지 순서대로 공백을 출력
#      3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자X를 출력한다.

n=int(input())
for i in range(1,n+1):
    if i%10==3 or i%10==6 or i%10==9:
        print('X',end=' ')
    else:
        print(i,end=' ')