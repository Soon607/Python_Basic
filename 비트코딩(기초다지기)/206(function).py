# 기준에 딸, 학생의 점수를 입력받아 학점을 리턴하는 함수 작성
# 90점 이상 ~ 100점 이하:A
# 80점 이상 ~ 90점 미만:B
# 70점 이상 ~ 80점 미만:C
# 60점 이상 ~ 70점 미만:D
# 60점 미만 :F

def grade(score):
    if (90<=score<=100):
        return 'A'
    elif (80<=score<90):
        return 'B'
    elif (70<=score<80):
        return 'C'
    elif (60<=score<70):
        return 'D'
    elif score<60:
        return 'F'
    
marks=int(input('Enter the score: '))
print('{}점은 학점{}'.format(marks,grade(marks)))