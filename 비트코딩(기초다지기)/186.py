# 각 자리수의 합이 20을 넘을 때까지 수를 계속 입력받는 프로그램

sum=0

while sum<=20:
    sum=0
    num=input('Enter the number: ')
    for i in num:
        sum+=int(i)
        
print('Finish')
