# 자연수 n을 입력 받아 1부터 n-1까지 각각의 수들을 5로 나눈 나머지들의 합을 리턴하는 함수작성하기

def fun(n):
    answer=0
    for i in range(1,n):
        answer+=i%5
        
    return answer

num=int(input('number:'))
print(fun(num))