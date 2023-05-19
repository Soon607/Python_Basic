n,m=input('Enter the number:').split(' ')
n,m=int(n),int(m)

def snail_array(n,m):
    array=[[0]*m for i in range(n)]
    
    directions=[(-1,0),(0,1),(1,0),(0,-1)]
    direction_idx=0
    current_row=n-1
    current_col=0
    
    for num in range(1,n*m+1):
        array[current_row][current_col]=num
        
        next_row=current_row+directions[direction_idx][0]
        next_col=current_col+directions[direction_idx][1]
        
        if next_row<0 or next_row>=n or next_col<0 or next_col>=m or array[next_row][next_col]!=0:
            direction_idx=(direction_idx+1)%4
            next_row=current_row+directions[direction_idx][0]
            next_col=current_col+directions[direction_idx][1]
        
        current_row=next_row
        current_col=next_col
        
    return array

def printarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print('%2d' %array[i][j],end=' ')
        print()
        
printarray(snail_array(n,m))