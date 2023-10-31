# 문자열을 입력 받아, 빠진 알파벳을 대문자로 순서대로 출력하는 프로그램
alphabet='ABCDEFGHIKLMNOPQRSTUVWXYZ'
alphabet=list(alphabet)
mystr=list(input('Enter the sentence:').upper())
for i in alphabet:
    if not (i in mystr):
        print(i,end='')