# 두 수 사이에 있는 3의 배수의합

a=int(input('Enter the 1st number:'))
b=int(input('Enter the 2nd number:'))

if a>b:
    c=a
    a=b
    b=c

sum=0
for i in range(a,b):
    if i%3==0:
        sum+=i
        
print(a,'부터',b,'까지 3의 배수의 합은',sum)

