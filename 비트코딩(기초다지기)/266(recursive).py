# fibo similar
def fibo_similar(n):
    if n in range(1,4):
        return 1
    else:
        return fibo_similar(n-1)+fibo_similar(n-3)
    
print(fibo_similar(9))