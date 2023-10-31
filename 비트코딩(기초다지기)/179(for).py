n=2018
i=1
sum=0
a=0
while (n>0):
    if (n%10==2):
        sum+=(n//10)*i+(a+1)
        
    elif (n%10>2):
        sum+=(n//10+1)*i
    
    else:
        sum+=(n//10)*i
        
    a+=i*(n%10)
    i*=10
    n//=10
    
print(sum)