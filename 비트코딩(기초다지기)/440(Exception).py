# 사용자지정 예외처리
class TestError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return self.value
    
try:
    raise TestError('직접만든 오류!')
except Exception as e:
    print(e)
    print(type(e))
    
 