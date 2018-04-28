#!/usr/bin/env python
# coding=utf-8


def decorator_func1(func):
    def inner(*args,**kwargs):
        print("inner func ====")
        func(*args,**kwargs)

    return inner

@decorator_func1
def test1(a , b):
    print(" test1 == ")
    print("a = %d , b = %d"%(a , b))

@decorator_func1
def test2():
    print(" test2 == ")

test1(1,2)
test2()

