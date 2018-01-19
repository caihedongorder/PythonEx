#!/usr/bin/env python
# coding=utf-8


from OpenGL.GLUT import *

from gamemodule import keyboardevent
from gamemodule import windows
from gamemodule import render

def Init(InGLRenderCreateFunc):
    glutInit()
    windows.Init()
    keyboardevent.Init()
    render.Init(InGLRenderCreateFunc)

def Loop():
    glutMainLoop()
