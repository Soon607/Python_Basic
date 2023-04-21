# 예외변수를 지정하여 예외관련 정보 얻기
try:
    print(3/0)
    
except BaseException as e:
    print(e)
    print(type(e))
    