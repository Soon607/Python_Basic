
def mul(a,b):
    return a*b

def fun(a,b):      # fun() 함수 안에 mul()함수 사용
    c=a+b+mul(a,b)
    print(c)
    
def max_num(a,b):
    if a>b:
        return a
    else:
        return b
    
fun(10,20)
print('bigger number is ',max_num(20,10))