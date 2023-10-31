# 두 수를 입력받고, 입력 받은 두 수 사이의 정수를 랜덤으로 출력하는 프로그램 작성
# (두 수 사이의 정수가 존재하지 않을 때에는 'no integer between two numbers' 출력)

import random

# 나의 방법
a,b=input('두 정수를 입력하시오: ').split(' ')
a=int(a)
b=int(b)

# 먼저 입력한 수가 크면 두 수의 위치 교환
if a>b:
    c=a
    a=b
    b=c
    
if abs(a-b)<=1:
    print('no integer between two variables')
    
else:                                 
    print(random.randrange(a+1,b))
    
# 또 다른 방법

# num1=int(input('num1:'))
# num2=int(input('num2:'))

# if abs(num1-num2)<=1:
#     print('no integer between two numbers')
    
# else:
#     ran_num=(min(num1,num2)+random.randrange(1,abs(num1-num2)))
#     print(ran_num)
    
