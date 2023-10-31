# 여러 에러문
list=[1,7,3,0,5]
def fun(num):
    return(list[num]/list[num+3])

try:
    fun(0)
except ZeroDivisionError:
    print('ZeroDivisionError')
except IndexError:
    print('IndexError')
else:
    print('No Error')
    
try:
    fun(3)
except ZeroDivisionError:
    print('ZeroDivisonError')
except IndexError:
    print('IndexError')
else:
    print('No Error')
