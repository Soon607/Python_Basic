# 3행 3열의 2차원 배열을 두 개 입력받아, 두 배열의 같은 위치값을 곱하여 도출된 새로운 값을 새로운 배열의 같은 위치에 저장한 후 출력

def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print('%2d' %arr[i][j], end=' ')
        print()
    
def mul_array(arr1,arr2):
    array=[[0]*3 for n in range(3)]
    for i in range(3):
        for j in range(3):
            array[i][j]=arr1[i][j]*arr2[i][j]
            
    return array

arr1=[[3,6,9],[8,5,2],[1,7,4]]
arr2=[[9,8,7],[6,5,4],[3,2,1]]
print_arr(mul_array(arr1,arr2))