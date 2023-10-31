# 다음 조건을 만족하는 프로그램 작성하기
# 1. fun1()함수는 ArithmeticError와 IndexError의 예외가 발생할 가능성이 있는 함수이다.
# 2. fun1()함수를 사용할 때, ArithmeticError가 발생하면 'Error Code 1'을 IndexError가 발생하면 'Error Code 2'를 출력한다.
# 3. 만약 예외가 발생하지 않으면 'No Error'를 출력한다.
# ArithmeticError-수의 연산과 관련된 에러

try:
    fun1()
except ArithmeticError:
    print('Error Code 1')
except IndexError:
    print('Error Code 2')
else:
    print('No Error')
