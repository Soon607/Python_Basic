# 이와 같은 규칙을 가진 배열 만들기
# 1. 첫 번째 행은 모두 1로 초기화 되어 있다.
# 2. n번째 행의 첫 번째 원소는 1이다.
# 3. n번째 행의 다른 원소들은 n-1번째 행의 바로 위의 원소와 대각선 왼쪽 위의 원소를 더한 값이다.

n=int(input('Enter the number:'))
array=[[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i==0 or j==0:
            array[i][j]=1
        else:
            array[i][j]=array[i-1][j]+array[i][j-1]
            
            
def printarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print('%5d' %array[i][j],end='')
        print()

printarray(array)