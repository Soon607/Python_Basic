num=input('Enter the number:')
isNum=True
numdot=0

for i in num:
    if i not in '0123456789':
        if i=='.':
            if i==num[0]:
                isNum=False
                break
            else:
                numdot+=1
                if numdot==2:
                    isNum=False
                    break
        else:
            isNum=False
            break

print(num,'is numbers?',isNum) 