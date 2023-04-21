# 색을 입력해서, 이것이 colors에 있는 원소와 중복이 된다면 'Sorry'를 출력
# 중복되는 원소가 없다면 colors에 원소를 추가해서 출력

colors=['red','orange','blue','green','white','black','dark blue','purple']

color=input('Enter the color:')

if color in colors:
    print('Sorry')
    
else:
    colors.append(color)
    print(colors)
