# 두 단어를 입력받아서 그 구성이 다르면 'not same'
# 구성이 같으면 'same' 출력하는 프로그램 작성
# abcd 와 cadb는 구성이 같다
# abef와 beac는 구성이 다르다

first_word=input('Enter first:')
second_word=input('Enter second:')

def composition(first,second):
    list1=list(first)
    list2=list(second)
    list1.sort()
    list2.sort()
    if len(list1)!=len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i]!=list2[i]:
                return False
        return True
        
if composition(first_word,second_word):
    print('Same')
else:
    print('not Same')