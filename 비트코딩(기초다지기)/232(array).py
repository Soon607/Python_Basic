# 수를 입력받아, 앞의 n개는 1부터 시작하는 홀수의 오름차순,
# 두의 n개는 2부터 시작하는 짝수의 오름차순을 원소로 가진, 길이 2n짜리 1차원 배열을 만드는 함수 작성하기

n=int(input('input='))

array=[0 for i in range(2*n)]

for i in range(0,n):
    array[i]=2*i+1

for j in range(0,n):
    array[2*n-1-j]=2+2*j
    
print(array)