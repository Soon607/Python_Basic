#소수표현1
num=int(input('Enter the number:'))

if num==1:
    print(num,'is not prime number')
    
for i in range(1,num):
    if num%i==0 and i!=1:
        print(num,'is not prime number')
        break
    if i==num-1:
        print(num,'is prime number')
