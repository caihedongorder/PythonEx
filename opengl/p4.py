#!/usr/bin/env python
# coding=utf-8

import sys
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


from gamemodule import render
from gamemodule import application

class GLRender(render.GLRenderBase):
    def __init__(self):
        pass
    def OnDrawFunc(self):
        glClear(GL_COLOR_BUFFER_BIT)
        # glLoadIdentity()
        # glTranslatef(0.5,0,0)
        # glRotatef(135,0,1,0)
        # glutWireTeapot(0.5)
        # glutSolidTeapot(0.5)
        glBegin(GL_QUADS)
        # glVertex3f(-0.50,0.5,0)
        # glVertex3f(0.50,0.5,0)
        # glVertex3f(0.50,-0.5,0)
        # glVertex3f(-0.50,-0.5,0)
        # 逆时针
        glVertex3f(-0.5,0.5,0)
        glVertex3f(-0.5,-0.5,0)
        glVertex3f(0.5,-0.5,0)
        glVertex3f(0.5,0.5,0)
        glEnd()
        glFlush()

start = time.clock()



application.Init(lambda : GLRender())
application.Loop()

