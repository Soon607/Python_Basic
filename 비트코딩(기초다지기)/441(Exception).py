# 예외처리문장 만들기
boolean=True

while boolean:
    try:
        num=int(input('Enter the number:'))
        if num==0:
            raise Exception
        
    except Exception:
        print('Do again(except 0)')
    
    else:
        boolean=False