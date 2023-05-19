# <n*m 행렬 규칙>
# <대각선으로 숫자 채우기>
n,m=input('Enter the number:').split(' ')
n,m=int(n),int(m)
array=[[0]*m for i in range(n)]

k=1
for num in range(0,n+m-1):
    i=0
    j=0
    a=array[i][j]
    while a!=0:  # 모서리 지점까지 채우기
        if j!=m-1:
            j+=1
            a=array[i][j]
        else:
            i+=1
            a=array[i][j]
            
    while i+j == num and n-1>=i>=0 and m-1>=j>=0: # 왼쪽 대각선 아래로 채우기
        array[i][j]=k
        i+=1
        j-=1
        k+=1
        
def printarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print('%5d' %array[i][j],end='')
        print()
        
printarray(array)