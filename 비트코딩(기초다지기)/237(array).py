# 공백을 포함한 문자열을 입력받아, 공백으로 문자열을 분리하여 번호와 함께 출력

mystr=input('Enter the sentence:').split()
for i in range(len(mystr)):
    print('{}. {}'.format(i+1,mystr[i]))
    
