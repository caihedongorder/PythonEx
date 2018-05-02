#!/usr/bin/python 
# coding=utf-8


import sys	
import wx
import time



class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)
        
        self.CreateStatusBar()
        self.GetStatusBar().SetFieldsCount(2)


        self.Bind(wx.EVT_MOTION,self.onMotion)
        
        #self.timer = wx.Timer(self)#创建定时器  
        #self.Bind(wx.EVT_TIMER, self.onTimer, self.timer)#绑定一个定时器事件  
        #self.timer.Start(1000)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER,self.onTimer,self.timer)
        self.timer.Start(1000)

    def onTimer(self,event):
        self.GetStatusBar().SetStatusText(str(time.asctime(time.localtime(time.time()))),i = 1)

    def onMotion(self,event):
        self.GetStatusBar().SetStatusText(str(event.Position))
        #self.GetStatusBar().SetStatusText("Position:({x},{y})".format(x = event.GetPosition().x,y = event.GetPosition().y))
        event.Skip()


class wxWidgetDemo_statusBarApp(wx.App):
    
    #初始化
    def OnInit(self):

        # 创建主窗口
        self.frame = myFrame(parent=None,id = wx.ID_ANY,title = "状态栏")
        # 显示主窗口
        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

def main():
    #创建app 对象
    app = wxWidgetDemo_statusBarApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
