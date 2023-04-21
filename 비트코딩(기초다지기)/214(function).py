# 아래의 조건을 만족하면서, 100000보다 작은 자연수 중 3 또는 5의 배수를 모두 더한 합을 출력하는 프로그램 작성
# 조건1: 3의 배수를 판정하는 함수 ismulThree(n)과 5의 배수를 판정하는 함수 ismulFive(n)을 정의하여 사용
# 조건2: 전체 코드의 줄은 15줄을 넘지 않는다.

def ismulThree(n):
    return n%3==0

def ismulFive(n):
    return n%5==0

sum=0
for i in range(1,100000):
    if ismulThree(i) or ismulFive(i):
        sum+=i

print(sum)
    
            
        