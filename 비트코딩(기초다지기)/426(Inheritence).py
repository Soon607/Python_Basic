# Stack 
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
    
    
stack=Stack()
stack.push(3)
stack.push(1)
stack.push(8)
print(stack.pop())
stack.push(3)
print(len(stack))
print(stack.pop())
print(stack.pop())
print(stack.items)