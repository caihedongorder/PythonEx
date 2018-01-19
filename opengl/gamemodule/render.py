#!/usr/bin/env python
# coding=utf-8

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def _OnDrawFunc():
    if GRender:
        GRender.OnDrawFunc()

class GLRenderBase:
    def __init__(self):
        pass
    def OnDrawFunc(self):
        pass

GRender = None
GRenderCreateFunc = None

def Init(InRenderCreateFunc):
    global GRender,GRenderCreateFunc
    GRenderCreateFunc = InRenderCreateFunc
    GRender = GRenderCreateFunc()
    glutDisplayFunc(_OnDrawFunc)
    pass

def Uninit():
    global GRender,RenderCreateFunc
    GRenderCreateFunc = None

def ReCreate():
    global GRender,RenderCreateFunc
    GRender = GRenderCreateFunc()
    glutDisplayFunc(_OnDrawFunc)
    
