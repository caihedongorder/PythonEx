#!/usr/bin/env python
# coding=utf-8

import sys
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

GIsFullScreen = False
windowID = -1

def Init():
    global windowID
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400,400)
    windowID = glutCreateWindow(b"first")
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

