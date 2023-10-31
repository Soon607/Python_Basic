# list의 i와 j번째 값을 교환해주는 함수 작성
# (나의 시행착오 코드)

# list=[5,1,7,2,6,3]
# def swap(i,j):
#     list[i]=list[j]
#     list[j]=list[i]
    
# i,j=3,5
# swap(i,j)
# print(list)


## 파이썬 swap기능을 이용

#첫번째 방법

list=[5,1,7,2,6,3]
def swap(i,j):
     swap=list[i]
     list[i]=list[j]
     list[j]=swap
    
i,j=3,5
swap(i,j)
print(list)

