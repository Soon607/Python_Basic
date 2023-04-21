def fun1(num1,num2):
    result1=num1/num2
    result2=num1-num2
    list=[num1,num2,result1,result2]
    return (list[int(abs(sum(list)))])

for i in range(2):
    try:
        fun1(i+1,i+2)
    except ArithmeticError:
        print('A')
    except IndexError:
        print('I')
    else:
        print('G')
