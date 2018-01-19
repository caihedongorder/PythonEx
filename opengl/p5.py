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
        self.startTime = time.clock()
        self.rotateSpeed = 90
        pass
    def OnDrawFunc(self,DeltaTime):
        glClear(GL_COLOR_BUFFER_BIT)
        escapeTime = time.clock() - self.startTime
        rotateAngle = self.rotateSpeed * escapeTime
        rotateAngle = DeltaTime * self.rotateSpeed
        print(rotateAngle)
        # glLoadIdentity()
        glRotatef(rotateAngle,0,1,0)
        # glTranslatef(0.5,0,0)
        # glRotatef(135,0,1,0)
        # glutWireTeapot(0.5)
        # glutSolidTeapot(0.5)
        glBegin(GL_TRIANGLES)
        # glVertex3f(-0.50,0.5,0)
        # glVertex3f(0.50,0.5,0)
        # glVertex3f(0.50,-0.5,0)
        # glVertex3f(-0.50,-0.5,0)
        # 逆时针
        glColor3f(1.0,0,0)
        glVertex3f(0.0,0.5,0)
        glColor3f(0.0,1.0,0)
        glVertex3f(0.5,-0.5,0)
        glColor3f(0.0,0,1.0)
        glVertex3f(-0.5,-0.5,0)
        glEnd()
        glFlush()

start = time.clock()



application.Init(lambda : GLRender())
application.Loop()

