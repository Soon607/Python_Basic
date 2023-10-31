class ParentOne:
    def func(self):
        print('ParentOne의 함수 호출!')
        
class ParentTwo:
    def func(self):
        print('ParentTwo의 함수 호출!')
        
class Child(ParentOne,ParentTwo):
    def childfunc(self):
        ParentOne.func(self)
        ParentTwo.func(self)
        
objectChild=Child()
objectChild.childfunc()
objectChild.func()