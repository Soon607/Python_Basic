in_Char=input('Enter the character:')

while True:
    layer=input('Enter the layer:')
    try:
        int_layer=int(layer)
        break
    except:
        print('숫자를 입력하세요')

char_Count=range(1,int_layer*2,2)
for i in range(int_layer):
    print(' ' * (int_layer-i),in_Char*char_Count[i])
