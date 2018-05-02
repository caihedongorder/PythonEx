#!/usr/bin/python 
# coding=utf-8


import sys	
import wx



class myFrame(wx.Frame):
    """
        截屏功能
    """
    def __init__(self,**kwargs):
       
        self.__bRecreateDisplayBuffer = True
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        
        btn = wx.Button(self,label = "Screen Shot")

        #创建显示缓冲区
        self.RecreateDisplayBuffer()
        
        self.Bind(wx.EVT_BUTTON,self.OnBtnScreenShot,btn)
        self.Bind(wx.EVT_SIZE,self.OnSize)
        self.Bind(wx.EVT_PAINT,self.OnPaint)
        self.Bind(wx.EVT_IDLE,self.OnIdle)

    def OnBtnScreenShot(self,event):
        screenDC = wx.ScreenDC()

        width,height = screenDC.GetSize()
        memdc = wx.MemoryDC(self.__buffer)
        memdc.Blit(0,0,width,height,screenDC,0,0)
        print("Screen Width:{width},Height:{height}".format(width = width , height = height))

        self.Refresh(eraseBackground=False)

    def OnSize(self,event):
        self.__bRecreateDisplayBuffer = True

    def OnIdle(self,event):
        if self.__bRecreateDisplayBuffer:
            self.__bRecreateDisplayBuffer = False
            self.RecreateDisplayBuffer()

    def OnPaint(self,event):
        if self:
            dc = wx.BufferedPaintDC(self,self.__buffer)

            

    def RecreateDisplayBuffer(self):
        size = self.GetClientSize()
        self.__buffer = wx.Bitmap(size.Width , size.Height)

        dc = wx.BufferedDC(None,buffer = self.__buffer)
        dc.SetBackground(wx.Brush("black"))
        dc.Clear();

class wxWidgetDemo_ScreenShotApp(wx.App):
    
    #初始化
    def OnInit(self):

        # 创建主窗口
        self.frame = myFrame(parent=None,id = wx.ID_ANY,title = "hello,screen shot")
        # 显示主窗口
        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

def main():
    #创建app 对象
    app = wxWidgetDemo_ScreenShotApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
