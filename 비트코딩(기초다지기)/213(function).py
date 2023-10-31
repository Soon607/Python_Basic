# 어떤 수 n이 입력되면 n의 각 자릿수의 합이 한 자리가 될 때까지 계산하여 출력하는 프로그램 작성

def add_all(n):
    sum=0
    while n!=0:
        sum+=n%10
        print('+',n%10,end='')
        n//=10
    print('=',sum)
    return sum    # 각 자리수 합 더하기

n=int(input('Enter the number:'))

while n//10!=0:  # 자릿수의 합 한자리로 만들어주기
    n=add_all(n) # n= add_all(n)의 return 값
