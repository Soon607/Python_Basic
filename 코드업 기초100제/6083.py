# 입력: 빨녹파(r, g, b) 각 빛의 가짓수가 공백을 두고 입력된다.
#      예를 들어, 3 3 3 은 빨녹파 빛에 대해서 각각 0~2까지 3가지 색이 있음을 의미한다.
#      0 <= r,g,b <= 127

# 출력: 만들 수 있는 rgb 색의 정보를 오름차순(계단을 올라가는 순, 12345... abcde..., 가나다라마...)으로
#      줄을 바꿔 모두 출력하고, 마지막에 그 개수를 출력한다.
 
r,g,b=input().split()
r,g,b=int(r),int(g),int(b)

for i in range(r):
    for j in range(g):
        for x in range(b):
            print(i,j,x)
print(r*g*b)