# 입력
# 정수 1개를 입력받는다.
# (1 ~ 100)

# 출력
# 1부터 입력한 정수보다 작거나 같을 때까지 1씩 증가시켜 출력하되
# 3의 배수는 출력하지 않는다.

n=int(input())
for i in range(1,n+1):
    if i%3==0:
        continue
    # if n<i:
    #     break
    print(i,end=' ')
    
