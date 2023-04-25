# exponential function
def exp(a,n):
    if n==0:
        return 1
    
    return a*exp(a,n-1)


print(exp(3,2))
print(exp(4,7))
