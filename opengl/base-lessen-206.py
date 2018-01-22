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
        glOrtho(0,application.winSize[0],0,application.winSize[1],-100,100)
        self.center = [application.winSize[0]*0.5,application.winSize[1]*0.5,0]
        self.r = 80
        self.vertices = []
        for i in range(0,360):
            self.vertices.extend([self.center[0]+self.r*math.cos(math.radians(i)),self.center[1]+self.r*math.sin(math.radians(i)),self.center[2]])
            self.vertices.extend([self.center[0]+self.r*math.cos(math.radians(i+1)),self.center[1]+self.r*math.sin(math.radians(i+1)),self.center[2]])

        self.vertices1 = []
        for i in range(0,361):
            self.vertices1.extend([self.center[0]+self.r*math.cos(math.radians(i)),self.center[1]+self.r*math.sin(math.radians(i)),self.center[2]])

        self.vertices2 = []
        for i in range(0,360):
            self.vertices2.extend([self.center[0]+self.r*math.cos(math.radians(i)),self.center[1]+self.r*math.sin(math.radians(i)),self.center[2]])
        # print(self.vertices)
        glEnableClientState(GL_VERTEX_ARRAY)


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

        # render circle
        r = 80
        center = [application.winSize[0]*0.5,application.winSize[1]*0.5,0]
        # glBegin(GL_TRIANGLES)
        # for i in range(0,360):
        #     glVertex3f(center[0],center[1],center[2])
        #     glVertex3f(center[0]+r*math.sin(math.radians(i)),center[1]+r*math.cos(math.radians(i)),center[2])
        #     glVertex3f(center[0]+r*math.sin(math.radians(i+1)),center[1]+r*math.cos(math.radians(i+1)),center[2])
        # glEnd()

        # glBegin(GL_TRIANGLE_FAN)
        # glVertex3f(center[0],center[1],center[2])
        # for i in range(0,360):
        #     glVertex3f(center[0]+r*math.cos(math.radians(i)),center[1]+r*math.sin(math.radians(i)),center[2])
        #     glVertex3f(center[0]+r*math.cos(math.radians(i+1)),center[1]+r*math.sin(math.radians(i+1)),center[2])
        # glEnd()
        # glVertexPointer(3,GL_FLOAT,12,self.vertices)
        # glDrawArrays(GL_LINES,0,int(len(self.vertices)/3))

        # glVertexPointer(3,GL_FLOAT,12,self.vertices1)
        # glDrawArrays(GL_LINE_STRIP,0,int(len(self.vertices1)/3))

        glVertexPointer(3,GL_FLOAT,12,self.vertices2)
        glDrawArrays(GL_LINE_LOOP,0,int(len(self.vertices2)/3))
        glutSwapBuffers()

start = time.clock()



application.Init(lambda : GLRender())
application.Loop()

