# 소수판별
num=int(input('Enter the number:'))

list1=[]

for i in range(1,10):
    if num%i==0:
        list1.extend(str(i))
        
        
if len(list1)==1:
    print('{} is prime number'.format(num))
    
else:
    print('{} is not prime number'.format(num))
