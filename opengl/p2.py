#!/usr/bin/env python
# coding=utf-8

import sys
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

start = time.clock()

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    # glLoadIdentity()
    # glTranslatef(0.5,0,0)
    # glRotatef(135,0,1,0)
    # glutWireTeapot(0.5)
    # glutSolidTeapot(0.5)
    glBegin(GL_TRIANGLES)
    glVertex3f(0,1.0,0)
    glVertex3f(-1,-1.0,0)
    glVertex3f(1,-1.0,0)
    glEnd()
    glFlush()

    print("time esclaped:%01f"%(time.clock()-start))

	
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400,400)
glutCreateWindow(b"first")
glutDisplayFunc(drawFunc)
glutMainLoop()
