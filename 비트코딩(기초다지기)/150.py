# 한 점을 구성하는 (x,y)좌표를 입력받고, 이 점이 (50,40),(50,80),(100,40),(100,80)을 꼭짓점으로 갖는 사각형 안에 있는지
# 판별하는 프로그램

x=int(input('x:'))
y=int(input('y:'))

if (50<x<100) and (40<y<80):
    print(True)
    
else:
    print(False)
