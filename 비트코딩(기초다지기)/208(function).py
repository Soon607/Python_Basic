# 반지름을 입력받아 원의 넓이를 출력하는 함수 surf(r)을 정의하여, 원의 반지름을 입력하면 넓이를 출력하는 프로그램을 작성하시오.

def surf(r):
    return 3.14*r**2

radius=int(input('Enter the radius:'))
print('The surface is {}'.format(surf(radius)))