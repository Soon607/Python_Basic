n,m=input('Enter the number:').split(' ')
n,m=int(n),int(m)
array=[[0]*m for i in range(n)]

k=n*m
for num in range(n+m-1):
    i=0
    j=0
    a=array[i][j]
    while a!=0:
        if j!=m-1:
            j+=1
            a=array[i][j]
        else:
            i+=1
            a=array[i][j]
    while i+j==num and m-1>=j>=0 and n-1>=i>=0:
        array[i][j]=k
        i+=1
        j-=1
        k-=1
        
def printarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print('%2d' %array[i][j],end=' ')
        print()
        
printarray(array)