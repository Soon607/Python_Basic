num=int(input('Enter the number:'))
array=[[0]*num for i in range(num)]

k=1
for i in range(num):
    if i%2==0:
        for j in range(num):
            array[j][i]=k
            k+=1
            
    else:
        for j in range(num-1,-1,-1):
            array[j][i]=k
            k+=1
            
def printarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print('%5d' %array[i][j],end='')
        print()
        
printarray(array)