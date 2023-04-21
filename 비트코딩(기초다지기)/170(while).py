# 두 수를 입력받아, 작은 수에서 큰 수까지 5의 배수를 순서대로 출력하는 프로그램을 작성하시오.

first_num=int(input('first num:'))
second_num=int(input('second num:'))

if first_num>second_num:
    c=first_num
    first_num=second_num
    second_num=c
    
i=first_num+1
while i<second_num:
    if i%5==0:
        print(i)
    i+=1