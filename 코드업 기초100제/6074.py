#입력: 영문자 1개가 입력된다.
#출력: a부터 입력한 문자까지 순서대로 공백을 두고 한 줄로 출력한다.
a=ord(input())
i=ord('a')
while i<=a:
    print(chr(i),end=' ')
    i+=1