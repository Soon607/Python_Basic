# 세 수를 입력받아 (가장 큰 수)*(가장 작은 수)-(중간 수)를 출력하는 프로그램

list_1=[]
a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))
list_1.extend([a,b,c])
list_1.sort()
print(list_1[2]*list_1[0]-list_1[1])
