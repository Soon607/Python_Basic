# 영어 문장을 하나 입력받아 처음 시작하는 알파벳이 모음이면 Good Sentence를 출력하는 프로그램 작성


sentence=input('type sentence:')

if sentence[0] in 'aeiouAEIOu':
    print(True)
    
else:
    print(False)
    
    
    
