#!/usr/bin/env python
# coding=utf-8


import sys
from OpenGL.GLUT import *

from gamemodule import keyboardevent
from gamemodule import windows
from gamemodule import render


winSize = [400,400]

def Init(InGLRenderCreateFunc,WindowTitle=None):
    glutInit(sys.argv)
    windows.Init(WindowTitle)
    keyboardevent.Init()
    render.Init(InGLRenderCreateFunc)


def Loop():
    glutMainLoop()
