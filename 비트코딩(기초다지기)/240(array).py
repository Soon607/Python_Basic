# 1. 1~10 자연수 N개가 띄어쓰기로 구분되어 입력된다.
# 2. 입력된 수들 중에서 1,2,.....10의 개수를 각각 세어서 출력한다.
# 위의 조건을 만족하여 무작위로 주어진 N개의 1이상 10이하의 자연수 중에서 각각의 개수를 세어 출력하는 프로그램 작성하기

number=input('Enter the numbers:').split(' ')
num=range(1,11)

def howmany(number):
    for i in range(len(num)):
        quantity=0
        for j in range(len(number)):
            if num[i]==int(number[j]):
                quantity+=1
        print('{} 의 갯수:{}'.format(i+1,quantity))
    
howmany(number)