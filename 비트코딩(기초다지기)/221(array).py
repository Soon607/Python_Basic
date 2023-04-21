# 2차원 배열 선언하기
# 반복문과 조건문 활용

matrix1=[]
for i in range(3):
    matrix1.append([i]*4)
print(matrix1)

matrix2=[[0]*3 for i in range(3)]
print(matrix2)

matrix3=[[0 for col in range(3)] for row in range(3)]
print(matrix3)

matrix4=list(i for i in range(10) if i%2==0)

values=[0,1,2,3,4]
matrix5=[v**2 for v in values]
print(matrix5)

matrix6=[v**2 for v in values if v%2==0]
print(matrix6)