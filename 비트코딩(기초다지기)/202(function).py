def add1(a,b):  # 두 수를 더해서, 더한 값을 출력
    print(a+b)
    
def add2(a,b): # 두 수를 더해서, 더한 값을 리턴
    return a+b

a=int(input('Enter the number: '))
b=int(input('Enter the number: '))

add1(a,b)
print(add2(a,b))

