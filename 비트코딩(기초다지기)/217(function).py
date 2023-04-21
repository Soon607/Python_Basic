# 숫자를 입력하면 셀프넘버인지 판별해 주는 프로그램을 작성하시오.

def d(n):  # 생성자 함수
    num=n  
    while n!=0:                  #n=33
        num+=n%10
        n=n//10
    return num                  #num=39

# 셀프넘버인지 판별해주는 함수
def isSelfnum(n):
    boolean=True
    for i in range(1,n):  
        if n==d(i):           # (자기자신+각자릿수)가 n이랑 같은게 있으면 0반환 없으면 1반환 
            boolean=False
    return boolean

n=int(input('Enter the number:'))
print(isSelfnum(n))
                   
