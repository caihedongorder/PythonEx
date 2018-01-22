#!/usr/bin/env python
# coding=utf-8

import sys
import time
import math

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
        # glMatrixMode(GL_MODELVIEW)
        # glLoadIdentity()
        # gluLookAt(0,0,10,0,0,0,0,1,0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        width = application.winSize[0]
        height = application.winSize[1]
        glOrtho(0,width,0,height,-100,100)
        self.vertices = [
                    0,height*0.5,0,
                    0,0,0,
                    width*0.5,height*0.5,0,
                    width*0.5,0,0
                ]

        # print(self.vertices)
        glEnableClientState(GL_VERTEX_ARRAY)


    def OnDrawFunc(self,DeltaTime):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        escapeTime = time.clock() - self.startTime
        rotateAngle = self.rotateSpeed * escapeTime
        rotateAngle = DeltaTime * self.rotateSpeed
        print(rotateAngle)
        glVertexPointer(3,GL_FLOAT,0,self.vertices)
        glDrawArrays(GL_TRIANGLE_STRIP,0,int(len(self.vertices)/3))
        glutSwapBuffers()

start = time.clock()



application.Init(lambda : GLRender())
application.Loop()

