a=10                                   # is 연산자: 같은 객체인지를 알려준다.
b=10                                   # == 연산자: 같은 값인지를 알려준다.
c=5+5
print(a is b,a==b)
print(a is c,a==c)

list1=[1,2,3]
list2=[1,2,3]
print(list1 is list2,list1==list2)

def fun1():
    print('1')
    
def fun2():
    print('2')
print(fun1 is fun2)

