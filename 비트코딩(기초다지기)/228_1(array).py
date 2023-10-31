import random

array=[[0]*5 for i in range(5)]
for i in range(25):
    array[i//5][i%5]=random.randrange(2,25)
    
sum=0
for i in range(5):
    for j in range(5):
        print('%2d' %array[i][j],end=' ')
        sum+=array[i][j]
    print()
    
if sum/25>=12.5:
    print('Big')
else:
    print('Small')