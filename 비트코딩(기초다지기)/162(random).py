# 10 이상 20 이하의 정수형 난수 4개를 발생시켜, 이들의 평균이 15이상이면 Big, 아니면 Small을 출력하는 프로그램 작성

import random

numbers=range(10,21) # 10 이상 20 이하의 정수형 난수

rand_num=[random.choice(numbers) for i in range(0,4)] # 랜덤으로 요소 4개 선택 (기억하기!)

print('4가지수:',rand_num)
mean=sum(rand_num)/len(rand_num)
print('평균:',mean)
if mean>=15:
    print('Big')

else:
    print('Small')
