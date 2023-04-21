# 자연수 N이 주어질 때, N을 제곱수들의 합으로 표현할 때에 그 표현들 중 최소 개수 조합들 중 하나를 리스트 타입으로 리턴하는 함수 만들기

def fun_Double(N):
    max=1
    while max**2<=N:  # N=14, max=3
        max+=1
    for i in range(max):
        for j in range(max):
            for k in range(max):
                if(i**2+j**2+k**2==N):
                    a=[i,j,k]
                    while 0 in a:
                        a.remove(0)
                    return a
                
    print('Sorry')
print(fun_Double(14))
