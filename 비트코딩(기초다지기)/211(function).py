# 최대공약수와 최소 공배수를 리턴 하는 함수를 작성하라
def GCD(n,m): #최대공약수
    if n<m:
        min=n
        
    else:
        min=m
        
    for i in range(min,0,-1):
        if n%i==0 and m%i==0:
            res=i
            break
    return res


def lcm(n,m):  #최소 공배수
    if n>m:
        max=n
    else:
        max=m
    for i in range(max,(n*m)+1):
        if i%n==0 and i%m==0:
         res=i
         break
    return res

n=int(input('Enter the 1st number: '))
m=int(input('Enter the 2nd number: '))
print('GCD of',n,'and',m,'is',GCD(n,m))
print('LCM of',m,'and',n,'is',lcm(m,n))

