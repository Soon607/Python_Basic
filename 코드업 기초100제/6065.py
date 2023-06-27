#입력: 3개의 정수 (a,b,c)가 공백을 두고 입력된다. (적어도 1개는 짝수이다.)
#출력: 짝수만 순서대로 줄을 바꿔 출력한다.
a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
if a%2==0:
    print(a)
    
if b%2==0:
    print(b)
    
if c%2==0:
    print(c)
    

