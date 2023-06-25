# 입력: 3개의 정수가 공백으로 구분되어 입력된다.
# 출력: 가장 작은 값을 출력한다.
a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
d=(a if (a<b) else b)if ((a if (a<b) else b)<c) else c
print(d)