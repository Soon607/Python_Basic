# 정수 n을 입력받았을 때, 1부터 n까지의 정수에 나오는 1의 총 개수를 구하는 프로그램을 작성하시오.
# ex) n=4일 때, 결과는 1 (1,2,3,4중 1은 1개)
# ex) n=13일때, 결과는 6 (1~13중 1은 6개) 1,2,3,4,5,6,7,8,9,10,11,12,13
def one(n):
    case=0
    for i in range(1,n+1): #1~n
        num=i
        while num!=0:
            if num%10==1: # 각 자리값이 1인지 체크
                case+=1
            num//=10
    return case

num=int(input('Enter the number:'))
print(one(num))
        
        
        