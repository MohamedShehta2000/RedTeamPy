class parent:
    def hi(self):
        x = 5
        print(x)
class child(parent):
    pass
childobj=child()
childobj.hi()

class parent:
    def __init__(self):
        self.hi()
    def hi(self):
        x = 5   
        print(x)
class child(parent):
    def __init__(self):
        super().__init__()
        print('hello')
childobj=child()
    
