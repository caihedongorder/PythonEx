#!/usr/bin/env python
# coding=utf-8

import sys
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

GIsFullScreen = False
windowID = -1

def Init( WindowTitle=None ):
    global windowID
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    from gamemodule import application
    glutInitWindowSize(application.winSize[0],application.winSize[1])
    windowID = glutCreateWindow( bytes(WindowTitle,encoding = 'utf-8') if WindowTitle else b'first')
    print("windowID:",windowID)

def Uninit():
    global windowID
    glutDestroyWindow(windowID)
    windowID = -1

def ReCreateWindow(bToggleFullScreen = True):
    global windowID,GIsFullScreen
    Uninit()
    Init()

    from gamemodule import render
    from gamemodule import keyboardevent
    render.ReCreate()
    keyboardevent.Init()
    if bToggleFullScreen:
        GIsFullScreen = not GIsFullScreen
        if GIsFullScreen:
            glutFullScreen()

