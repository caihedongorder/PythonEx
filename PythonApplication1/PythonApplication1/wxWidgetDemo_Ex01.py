#!/usr/bin/python 
# coding=utf-8


import sys	
import wx



class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       self.__needRecreateBitmap = True
       #构造基类方法
       super(myFrame, self).__init__(**kwargs)

       self.createDisplayBitmap()

       btn = wx.Button(self,label = "截图")
       self.Bind(wx.EVT_BUTTON,self.onSnipScreen,btn)

       btn1 = wx.Button(self,label = "Screen Shot")
       self.Bind(wx.EVT_BUTTON,self.onSnipScreen,btn1)


       self.Bind(wx.EVT_IDLE,self.onIdle)
       self.Bind(wx.EVT_PAINT,self.onPaint)
       self.Bind(wx.EVT_SIZE,self.onSize)
       
    def createDisplayBitmap(self):
        size  = self.GetClientSize()
        self.__bitmap = wx.Bitmap( size )

        dc = wx.BufferedDC(None,buffer = self.__bitmap)
        dc.SetBackground(wx.Brush("black"))
        dc.Clear()
        
        self.Refresh( eraseBackground= False )
    def onPaint(self,event):
        if self:
            wx.BufferedPaintDC(self,buffer = self.__bitmap)

    def onIdle(self,event):
        if self.__needRecreateBitmap:
            self.createDisplayBitmap()
            self.__needRecreateBitmap = False

    def onSize(self,event):
        self.__needRecreateBitmap = True

    def onSnipScreen(self,event):
        screenDc = wx.ScreenDC()
        screenSize = screenDc.GetSize()

        memDc = wx.MemoryDC(self.__bitmap)

        frameSize = self.GetClientSize()
        memDc.Blit(0,0,frameSize.Width,frameSize.Height,screenDc,0,0)

        self.Refresh(eraseBackground = False)


class wxWidgetDemo_Ex01App(wx.App):
    
    #初始化
    def OnInit(self):

        # 创建主窗口
        self.frame = myFrame(parent=None,id = wx.ID_ANY,title = "截屏练习")
        # 显示主窗口
        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

def main():
    #创建app 对象
    app = wxWidgetDemo_Ex01App()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
