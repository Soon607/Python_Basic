# 회문인지 아닌지 판단해주는 프로그램

def is_palindrome(word):
    if len(word)<2:
        return True
    if word[0]!=word[-1]:
        return False
    return is_palindrome(word[1:-1])

str=input('Enter the sentence:')
print(is_palindrome(str))
        