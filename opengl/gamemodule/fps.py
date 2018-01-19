#!/usr/bin/env python
# coding=utf-8

import time


class FPS:
    def __init__(self):
        self.startTime = time.clock()
        self.drawCount = 0;
    def increase(self):
        self.drawCount +=1
    def reset(self):
        self.startTime = time.clock()
        self.drawCount = 0 
    def print(self):
        print("FPS:%d"%(self.drawCount / (self.DeltaTime())))
    def DeltaTime(self):
        return time.clock()-self.startTime
