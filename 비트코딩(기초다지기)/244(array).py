# n개의 숫자가 입력되면 n개의 숫자를 왼쪽으로 한 자리씩 순서대로 shift하는 배열을 출력
num=input('Enter the numbers:').split()
array=[[0]*len(num) for i in range(len(num))]

for i in range(len(array)):
    for j in range(len(array)):
        if i==0:
            array[i][j]=int(num[j])
        else:
            array[i][j-1]=array[i-1][j]
            

def printarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print('%2d' %array[i][j],end='')
        print()
        
printarray(array)