a=int(input('Enter the 1st number:'))
b=int(input('Enter the 2nd number:'))

if a>b:
    c=a
    a=b
    b=c

sum=0
for i in range(a,b+1):
    if i%2==0:
        sum-=i
        print('-{}'.format(i),end='')
    else:
        sum+=i
        print('+{}'.format(i),end='')

print('={}'.format(sum))
    
        