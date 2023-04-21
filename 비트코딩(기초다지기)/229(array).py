# 문자열을 입력받아 대문자와 소문자의 수를 구하는 프로그램
sentence=input('Enter the sentence:')

def numOfupp(str):
    num=0
    for i in range(len(str)):
        if 'A'<=str[i]<='Z':
            num+=1
    return num

def numOflow(str):
    num=0
    for i in range(len(str)):
        if 'a'<=str[i]<='z':
            num+=1
    return num

print('Upper:',numOfupp(sentence),end=' ')
print('Lower:',numOflow(sentence))