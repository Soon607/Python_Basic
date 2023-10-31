# n부터 1까지 1씩 내려가는 함수 재귀적으로 작성하기

def countdown(n):
    if n==0:
        print('-end-')
    else:
        print(n)
        countdown(n-1)

num=int(input('Enter the number:'))
countdown(num)