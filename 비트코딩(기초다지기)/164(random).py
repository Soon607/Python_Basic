# cars 라는 이름의 리스트에 Hyundai, Kia, BMW, Benz를 원소로 저장한다.
# 이 리스트를 random 모듈의 함수를 이용하여 섞어준다.
# 그 다음, 가장 첫 번째의 원소가 Hyundai라면 True를 출력하는 프로그램을 작성한다.

import random

cars=['Hyundai','Kia','BMW','Benz']

print('original:',cars)

random.shuffle(cars)

print('change:',cars)

if cars[0]=='Hyundai':
    print(True)
    
else:
    print(False)