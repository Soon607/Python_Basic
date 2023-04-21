import random

list1=['a','b','c','d']
print(list1)

# random.shuffle(list): list의 순서를 랜덤 섞기
random.shuffle(list1)
print(list1)
random.shuffle(list1)
print(list1)

# list 요소를 랜덤 선택
chr1=random.choice(list1)
print(chr1)

