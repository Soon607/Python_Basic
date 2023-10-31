# 정수를 입력 받았을 때, 입력값이 0~9까지의 숫자가 모두 각각 한번씩만 
# 사용된것인지 확인하는 함수를 작성

def allnum(n):
    for i in range(0,10):
        case=0
        num=n
        while num!=0:  #9614308527
            if num%10==i:
                case+=1
            num=num//10
        if case!=1:   #중복되었는지 확인
            return False
    return True

n=int(input('Enter the number:')) #1234567890, 9614308527
print(allnum(n))