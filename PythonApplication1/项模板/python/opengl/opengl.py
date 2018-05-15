#!/usr/bin/env python
# coding=utf-8

import sys
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


from gamemodule import render
from gamemodule import application

class $safeitemname$GLRender(render.GLRenderBase):
    def __init__(self):
        render.GLRenderBase.__init__(self)

    def OnDrawFunc(self,DeltaTime):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glutSwapBuffers()

def main():
    start = time.clock()
    application.Init(lambda : $safeitemname$GLRender(),WindowTitle = '$safeitemname$')
    application.Loop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))

