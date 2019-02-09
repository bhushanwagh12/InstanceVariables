# inside a instance method by using self variable
class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=90
        print(self.__dict__)
t=Test()
t.m1()
