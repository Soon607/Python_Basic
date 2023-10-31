# 입력: 정수 1개가 입력된다.
# 출력: 1부터 그 수까지 짝수만 합해 출력한다.
n=int(input())
s=0
for i in range(n+1):
    if i%2==0:
        s+=i
    else:
        continue
    
print(s)
    