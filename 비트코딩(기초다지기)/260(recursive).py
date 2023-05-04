# Collatz conjecture
def collatz(n):
    print(n,end=' ')
    if n==1:
        return 1
    elif n%2==0:
        collatz(n//2)
    else:
        collatz(3*n+1)
        
collatz(5)