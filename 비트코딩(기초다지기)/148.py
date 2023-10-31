
year=int(input('year: '))

if (year%4==0):
    print('윤년')
    
elif (year%4==0) and (year%100==0):
    print('평년')
    
elif (year%400==0):
    print('윤년')
    
