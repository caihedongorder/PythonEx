#!/usr/bin/env python
# coding=utf-8

import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    # glLoadIdentity()
    glTranslatef(0.5,0,0)
    glRotatef(135,0,1,0)
    glutWireTeapot(0.5)
    # glutSolidTeapot(0.5)
    glFlush()

	
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400,400)
glutCreateWindow(b"first")
glutDisplayFunc(drawFunc)
glutMainLoop()
