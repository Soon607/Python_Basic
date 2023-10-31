# 문장을 입력하면 암호문으로 바꾸기
cryplist=[[0]*27 for i in range(2)]
cryplist[0]=['a','b,','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
cryplist[1]=['k','l','y','d','h','n','s','z','m','a','r','q','g','x','c','u','j','b','t','v','o','e','l','p','f','w','*']

def ChangetoSecret(str):
    list=[0]*len(str)
    for i in range(len(str)):
        for j in range(27):
            if str[i]==cryplist[0][j]:
                list[i]=cryplist[1][j]
                break
            elif str[i]==cryplist[0][j].upper():
                list[i]=cryplist[1][j].upper()
                break
    return list

def printlist(list):
    for i in list:
        print(i,end='')

sentence=input('Enter the sentence:')
printlist(ChangetoSecret(sentence))
