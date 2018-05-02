#!/usr/bin/python 
# coding=utf-8


import sys	
import wx
import math
import random



class myFrame(wx.Frame):

    def __init__(self,**kwargs):

        self.__color = "red"
        self.__thickness = 1
        self.__pen = wx.Pen(self.__color,self.__thickness)
        self.__lines = []
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        # 创建显示缓冲区
        self.createDisplayBuffer()
        
        self.Bind(wx.EVT_LEFT_DOWN,self.OnLeftDown,self)
        self.Bind(wx.EVT_LEFT_UP,self.OnLeftUp,self)
        self.Bind(wx.EVT_MOTION,self.OnMotion,self)
        self.Bind(wx.EVT_IDLE,self.OnIdle)
        self.Bind(wx.EVT_PAINT,self.OnPaint)
        self.Bind(wx.EVT_SIZE,self.OnSize)

    def createDisplayBuffer(self):
        size = self.GetClientSize();
        self.__buffer = wx.Bitmap(size.width,size.height)

        # 清空 缓冲区
        dc = wx.BufferedDC(None,self.__buffer)
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        
        self.drawLines(dc)

    def OnLeftDown(self,event):
        print("LeftButtonDown:{Position}".format(Position =  event.Position))
        self.__startPosition = event.Position
        self.__currentLines = []
        self.__currentLines.append(self.__startPosition)

        #随机产生颜色

        self.__color = ["red","green","blue"][ random.randint(0,2)];
        print("current Color:{color}".format(color = self.__color))
        
        self.__thickness = random.randint(1,3)
        #self.__thickness = 10

        self.__pen = wx.Pen(self.__color,self.__thickness)
        self.CaptureMouse()

    def OnMotion(self,event):
        if event.Dragging() and event.LeftIsDown():
            dc = wx.BufferedDC(None,buffer = self.__buffer)
            #dc = wx.ClientDC(self)
            dc.SetPen(self.__pen)
            dc.DrawLines([self.__startPosition,event.Position])
            self.__startPosition = event.Position
            self.__currentLines.append(self.__startPosition)

            self.Refresh(eraseBackground= False)
        event.Skip()

    def OnLeftUp(self,event):
        print("LeftButtonUp:{Position}".format(Position =  event.Position))
        self.__lines.append( { "pen":wx.Pen(self.__color,self.__thickness) , "lines" :self.__currentLines})
        self.__currentLines = None
        self.ReleaseMouse()

    def OnIdle(self,event):
        if self.__bRecreateDisplayBuffer:
            self.createDisplayBuffer()
            self.__bRecreateDisplayBuffer = False
    def OnPaint(self,event):
        #dc = wx.PaintDC(self)
        wx.BufferedPaintDC(self,self.__buffer)

    #绘制所有线
    def drawLines(self,dc):
        for line in self.__lines:
            dc.SetPen( line["pen"] )
            dc.DrawLines( line["lines"] )

    def OnSize(self,event):
        self.__bRecreateDisplayBuffer = True

class wxWidgetDemo_SketchWindowApp(wx.App):
    
    #初始化
    def OnInit(self):

        # 创建主窗口
        self.frame = myFrame(parent=None,id = wx.ID_ANY,title = "Skectch Window")
        # 显示主窗口
        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

def main():
    #创建app 对象
    app = wxWidgetDemo_SketchWindowApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
