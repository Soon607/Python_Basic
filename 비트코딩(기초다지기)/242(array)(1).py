# 정수를 차례로 입력하다가 0 이 입력되건, 입력된 정수가 100개를 초과하면 0을 제외하고 
# 그 때까지 입력된 정수를 가장 나중에 입력된 정수부터 차례대로 출력하는 프로그램 작성하기
stack = []
count = 0

while count < 100:
    num = int(input('Enter the number:'))
    if num == 0:
        break
    stack.append(num)
    count += 1

while stack:
    print(stack.pop(), end=' ')