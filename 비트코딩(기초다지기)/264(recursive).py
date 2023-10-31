# 10진수 2진수 변환
def to_bin(n):
    if n==1:
        return '1'
    ans=''
    while True:
        ans+=str(n%2)
        n=(n-n%2)//2
        
        if n in range(2):
            ans+=str(n)
            return ans[::-1]
        
print(to_bin(12))