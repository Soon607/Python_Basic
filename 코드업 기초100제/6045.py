# 입력: 정수 3개가 공백을 두고 입력된다.
# 출력: 합과 평균을 공백을 두고 출력한다. (평균은 소숫점 이하 셋째 자리에서 반올림한다.)
a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
print(a+b+c,format((a+b+c)/3,'.2f'))