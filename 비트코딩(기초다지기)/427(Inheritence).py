# stack을 이용해서 괄호 문제 풀기
class Stack:
    def __init__(self):
        self.items=[]
        
    def push(self,val):
        self.items.append(val)
        
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print('Stack is Empty')
            
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print('Stack is Empty')
            
    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self)==0
    
def expr(text):
    a=Stack()
    for i in text:
        if i=='(':
            a.push(i)
        if i==')':
            if a.isEmpty():
                return False
            else:
                a.pop()
        else:
            continue
    if a.isEmpty():
        return True
    else:
        return False
    
string=input('Enter the sentence:')
print(expr(string))