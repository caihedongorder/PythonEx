
import PythonApplication1

import os


c = PythonApplication1.test();

c.a = 100
c.b = 101

class test1(PythonApplication1.test):
    def __init__(self):
        self.c = 100
        return super(test1, self).__init__()

d = test1()

d.a = 100
d.b = 100
d.c = 10
print("a:{c.a},b:{c.b}".format(c = c))