# 난수를 생성한 후, 사용자가 입력한 숫자가 난수보다 큰지 작은지를 알려주고 
# 계속 추측해서 난수값을 맞추게 하는 프로그램

import random

n=random.randrange(1,100)
while True:
    ans1=input('Guess number (Q to exit):')
    if ans1.upper()=='Q':
        break
    ans2=int(ans1)
    if (n==ans2):
        print('Correct')
        break
    elif (n>ans2):
        print('choose higher number')
        
    else:
        print('choose lower number')
