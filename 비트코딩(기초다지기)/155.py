# 조건: 프로그램은 4개의 3항 연산자를 포함한다.
# 조건을 만족하면서, 하나의 정수를 입력받아 음수/양수인지, 홀수/짝수인지, 3의 배수인지/아닌지 5의 배수인지/아닌지를
# 판별해주는 프로그램 작성하기

number=int(input('enter: '))

print('양수') if number>0 else print('음수')
print('홀수') if number%2 !=0 else print('짝수')
print('3의 배수') if number%3==0 else print('3의 배수 아님')
print('5의 배수') if number%5==0 else print('5의 배수 아님')
