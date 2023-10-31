# 규칙에 따른 프로그램 만들기 (길이가 10인 1차원 배열)
# 1. 10미만의 자연수 두 개를 입력받아서 첫 번째 원소와 두 번째 원소를 입력받은 수로 초기화 한다.
# 2. 세 번째 원소부터 마지막 원소까지는 전전항과 전항을 곱한 값의 1의 자리이다.


array=[0 for i in range(10)]
a,b=input('Enter the two numeber:').split(' ')
a=int(a)
b=int(b)

array[0]=a
array[1]=b

for i in range(2,len(array)):
    array[i]=array[i-2]*array[i-1]%10
    
print(array)