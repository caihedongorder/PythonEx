#!/usr/bin/env python
# coding=utf-8

import time

class Timer:
    def __init__(self):
        self.timeLastTick = time.clock()
        self.currentTime = time.clock()

    def tick(self):
        self.timeLastTick = self.currentTime
        self.currentTime = time.clock()

    def DeltaTime(self):
        return self.currentTime - self.timeLastTick 
