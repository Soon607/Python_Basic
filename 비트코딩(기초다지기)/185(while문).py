
num=int(input('Enter the number: '))
len=1

while num!=1:
    
    if num%2==0:
        num=num/2
        
    else:
        num=2*num+2
        
    len+=1
    
print(len)
