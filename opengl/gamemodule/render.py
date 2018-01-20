#!/usr/bin/env python
# coding=utf-8

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



from gamemodule import fps
from gamemodule import timer
GFPS = fps.FPS()
GTimer = timer.Timer() 

def _OnDrawFunc():
    global GStartTime,GDrawCount,GFPS,GTimer
    
    GTimer.tick()
    if GRender:
        GRender.OnDrawFunc(GTimer.DeltaTime())

        if GFPS.DeltaTime() > 1.0:
            GFPS.reset()
        GFPS.increase()
        GFPS.print()

class GLRenderBase:
    def __init__(self):
        glClearColor(0,0,0,0)
        pass
    def OnDrawFunc(self,DeltaTime):
        pass

GRender = None
GRenderCreateFunc = None

def Init(InRenderCreateFunc):
    global GRender,GRenderCreateFunc
    GRenderCreateFunc = InRenderCreateFunc
    GRender = GRenderCreateFunc()
    glutDisplayFunc(_OnDrawFunc)
    glutIdleFunc(_OnDrawFunc)

def Uninit():
    global GRender,RenderCreateFunc
    GRenderCreateFunc = None

def ReCreate():
    global GRender,RenderCreateFunc
    GRender = GRenderCreateFunc()
    glutDisplayFunc(_OnDrawFunc)
    glutIdleFunc(_OnDrawFunc)
    
