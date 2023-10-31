# 숙제를 제출한 학생과 제출하지 않은 학생 구분

submission=input('숙제를 제출한 출석번호:').split(' ')

student_num=range(1,21)

non_submission=[]

for i in student_num:
    if str(i) in submission:
        continue
    else:
        non_submission.append(i)
        
for j in non_submission:
    print(j,end=' ')
    

