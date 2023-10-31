#입력: 정수 1개가 입력된다.
#출력: 음수이면서 짝수이면, A
# 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C
# 양수이면서 홀수이면, D
num=int(input())
if num<0:
    if num%2==0:
        print('A')
    else:
        print('B')
        
else:
    if num%2==0:
        print('C')
    else:
        print('D')