import os

print type(os)

class test(object):
    def __init__(self):
        self.a = 0
        self.b = 2

c = test()

c.a = 100
c.b = 101

print("a:{a},b:{b}".format(a = c.a,b = c.b))

print("hello World")