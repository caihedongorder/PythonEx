#!/usr/bin/env python
# coding=utf-8


import sys
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from gamemodule import windows
from gamemodule import application


def OnKeyboardPress(inKey,x,y):
    print("inKey:%d,x:%d,y:%d",(inKey,x,y))
    if inKey == b"q":
        sys.exit()
    elif inKey == b"\r":
        windows.ReCreateWindow()

def Init():
    glutKeyboardUpFunc(OnKeyboardPress)

