# 문장이 거꾸로 읽으나 제대로 읽으나 똑같은지 확인

def isHandsome(str):
    for i in range(len(str)):
        if str[i]!=str[len(str)-1-i]:
            return False
    return True

str=input('Enter the sentence:')
print(isHandsome(str))