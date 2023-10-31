# 1부터 입력한 숫자 n까지의 합을 구하는 프로그램

num=int(input('정수를 하나 입력하시오:'))
sum=0

for i in range(1,num+1):
    sum+=i
    
print('1 부터 {} 까지의 합은 {}'.format(num,sum))