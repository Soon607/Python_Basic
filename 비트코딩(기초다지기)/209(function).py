# 문장을 입력받아서 각 알파벳을 대문자로 바꾼후, 문장을 이루는 각 단어를 저장한 리스트를 반환하는 함수

def wordlist(string):
    string=str.upper(string)
    return string.split(' ')

string=input('Enter the sentence:')
print(wordlist(string))

# 더 간단한하게 만들어보자

# def wordlist(string):
#     return string.upper().split(' ')
