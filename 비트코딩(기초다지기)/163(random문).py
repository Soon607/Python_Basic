
import random

first_num=1
second_num=2
level=0

while level<3:
    level+=1
    ans=random.randrange(first_num,second_num+1)
    num=int(input('level{} ({}~{}):'.format(level,first_num,second_num)))
    if num==ans:
        print('Correct!')
        second_num=second_num*2
    else:
        print('Faliure')
        print('Answer is:',ans)
        break
if second_num>8:
    print('Lucky')
