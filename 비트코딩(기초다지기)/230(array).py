# 문자열을 거꾸로 출력하는 프로그램
# without reverse()

# 첫 번째 방법
# string=input('Enter the sentence:')
# print(string[::-1])

# for문 이용
string=input('Enter the sentence:')
def rev_str(str):
    mylist=list(str)
    for i in range(len(str)//2):
        a=mylist[len(str)-1-i]
        mylist[len(str)-1-i]=mylist[i]
        mylist[i]=a
        
    for i in range(len(str)):
        print(mylist[i],end='')

rev_str(string)
