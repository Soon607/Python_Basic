# return even numbers between two numbers

def evennum(a,b):
    if a>=b+2:
        evennum(b,a)
    elif (b-a)//2>0 and a%2==1:
        print(a+1,end=' ')
        evennum(a+2,b)
    
    elif (b-a)//2>0 and a%2==0:
        evennum(a+1,b)
        
evennum(5,3)