# 입력한 수의 각 자리수를 더하는 프로그램 작성

num=int(input('Enter the number:'))

sum=0
for i in str(num):
    sum+=int(i)
print(sum)
    
