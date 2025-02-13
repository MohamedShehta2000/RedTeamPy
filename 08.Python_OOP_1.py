#!/usr/bin/env python3
class newclass:
    def sum(self):
        print('hello')
object1 = newclass()
print(object1.sum())


class newclass:
    def sum(self):
        x = 4
        self.x = x
    def app(self):
        print(self.x)
object1 = newclass()    
object1.sum()
object1.app()

class newclass:
    def __init__(self):
        print('hello')
        self.sum()
    def sum(self):
        print(4+56)
object1 = newclass()
