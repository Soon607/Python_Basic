# n부터 1까지 1씩 내려가는 함수 재귀적으로 작성하기

def countdown(n):
    print(n)
    countdown(n-1) if n>1 else None
    
countdown(5)
