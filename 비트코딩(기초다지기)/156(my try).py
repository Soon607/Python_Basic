# 정수 2개와 사칙연산자(+,-,*,/)가 각각 공백을 사이에 두고 주어지는 경우, 해당 연산의 결과를 출력하는 프로그램

pro=input('Enter:')

if '+' in pro:
        print(int(pro[0])+int(pro[2]))
elif '-' in pro:
        print(int(pro[0])-int(pro[2]))
elif '*' in pro:
        print(int(pro[0])*int(pro[2]))
        
elif '/' in pro:
        print(int(pro[0])/int(pro[2]))

    
        
                      
