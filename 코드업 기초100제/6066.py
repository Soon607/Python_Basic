#입력: 3개의 정수가 공백을 두고 입력된다.
#출력: 입력된 순서대로 even/odd을 줄을 바꿔 출력한다.
a,b,c=input().split()
a,b,c=int(a),int(b),int(c)

if a%2==0:
    print('even')
else:
    print('odd')
    
if b%2==0:
    print('even')
else:
    print('odd')
    
if c%2==0:
    print('even')
else:
    print('odd')