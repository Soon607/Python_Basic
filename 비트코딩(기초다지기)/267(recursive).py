def hanoi(n,start,through,destination):
    if n==1:
        print(start,'->',destination)
    else:
        hanoi(n-1,start,destination,through)
        hanoi(1,start,through,destination)
        hanoi(n-1,through,start,destination)
        
hanoi(3,'A','B','C')