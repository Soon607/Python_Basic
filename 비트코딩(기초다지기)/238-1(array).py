numbers=input('숙제를 제출한 출석번호:').split(' ')
stnum=[1]*20

for i in range(20):
    for j in range(len(numbers)):
        if i+1==int(numbers[j]):
            stnum[i]=0
            
for i in range(20):
    if stnum[i]==1:
        print(i+1,end=' ')