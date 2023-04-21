num1=input().split(' ')
num2=input().split(' ')
num3=input().split(' ')

array=[[0]*2 for i in range(3)]
array[0]=[int(num1[0]),int(num1[1])]
array[1]=[int(num2[0]),int(num2[1])]
array[2]=[int(num3[0]),int(num3[1])]

print('가로 평균:',end='')
for i in range(3):
    print((array[i][0]+array[i][1]//2),end='')
print()

print('세로평균:',end='')
sum1=0
for i in range(3):
    sum2=0
    for j in range(2):
        sum2+=array[i][j]
    sum1+=sum2
    print(sum2//3,end='')
print()

print('전체평균:',sum2//6)