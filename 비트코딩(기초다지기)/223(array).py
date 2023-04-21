# 기초
array=[[0]*3 for i in range(3)]
for i in range(3):
    for j in range(3):
        array[i][j]=i+j
        
for i in range(3):
    print(array[i])