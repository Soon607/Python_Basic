# Collatz conjecture

def collatz(n):
    len=1
    if n==1:
        return 1
    elif n%2==0:
        len+=collatz(n//2)
    else:
        len+=collatz(3*n+1)
    return len

a,b=input('Enter the number:').split()
a,b=int(a),int(b)
if a>b:
    temp=a
    a=b
    b=temp
max=1
max_i=a+1
for i in range(a+1,b):
    if collatz(i)>max:
        max=collatz(i)
        max_i=i
print(max_i)