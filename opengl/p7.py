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
        render.GLRenderBase.__init__(self)
        self.startTime = time.clock()
        self.rotateSpeed = 90
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0,0,10,0,0,0,0,1,0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60,1,1,1000)
        glTranslatef(-1,1,0)

    def OnDrawFunc(self,DeltaTime):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        escapeTime = time.clock() - self.startTime
        rotateAngle = self.rotateSpeed * escapeTime
        rotateAngle = DeltaTime * self.rotateSpeed
        print(rotateAngle)
        # glLoadIdentity()
        # glRotatef(rotateAngle,0,1,0)
        # glTranslatef(0.5,0,0)
        # glRotatef(135,0,1,0)
        # glutWireTeapot(2)
        glMatrixMode(GL_MODELVIEW)
        glRotatef(self.rotateSpeed*DeltaTime,0,1,0)
        glBegin(GL_TRIANGLES)
        glColor3f(1,0,0)
        glVertex3f(0,1,0)
        glColor3f(0,1,0)
        glVertex3f(-1,-1,0)
        glColor3f(0,0,1)
        glVertex3f(1,-1,0)
        glEnd()
        glutSwapBuffers()

start = time.clock()



application.Init(lambda : GLRender())
application.Loop()

