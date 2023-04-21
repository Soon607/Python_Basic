array = [0] * 100
i = 0

while i < 100:
    num = int(input('Enter the number:'))
    if num == 0:
        break
    array[i] = num
    i += 1

for j in range(i - 1, -1, -1):
    print(array[j], end=' ')
