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
        self.rotateSpeed = 180

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0,0,10,0,0,0,0,1,0)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60,1,1,1000)

    def OnDrawFunc(self,DeltaTime):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glRotatef(self.rotateSpeed * DeltaTime,0,1,0)
        glutWireTeapot(2)
        glutSwapBuffers()

start = time.clock()



application.Init(lambda : GLRender())
application.Loop()

