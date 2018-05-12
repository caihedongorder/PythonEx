#!/usr/bin/python 
# coding=utf-8


import sys	
import wx



class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        self.scroll = wx.ScrolledWindow(self)
        self.scroll.SetScrollbars(4,4,100,100)

        btn1 = wx.Button(self.scroll,label="Scroll To Top",pos = (320,370) )
        self.Bind(wx.EVT_BUTTON,self.onScrollToTop,btn1)

        btn2 = wx.Button(self.scroll,label="Scroll To Bottom")
        self.Bind(wx.EVT_BUTTON,self.onScrollToBottom,btn2)

        #self.scroll.FitInside()

    def onScrollToTop(self,event):
        self.scroll.Scroll(1,1)
    def onScrollToBottom(self,event):
        self.scroll.Scroll(100,100)

class wxWidgetDemo_ScrollApp(wx.App):
    
    #初始化
    def OnInit(self):

        # 创建主窗口
        self.frame = myFrame(parent=None,id = wx.ID_ANY,title = "Scroll Window")
        # 显示主窗口
        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

def main():
    #创建app 对象
    app = wxWidgetDemo_ScrollApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
