#!/usr/bin/python 
# coding=utf-8


import sys	
import wx



class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        self.sp = wx.SplitterWindow(self,style = wx.SP_NOBORDER)

        #样式 一定要设置
        self.p1 = wx.Panel(self.sp,style = wx.SUNKEN_BORDER)
        self.p2 = wx.Panel(self.sp,style = wx.SUNKEN_BORDER)
        self.p2.Hide()
        
        self.p1.SetBackgroundColour('pink')
        self.p1.SetBackgroundColour('skyblue')

        self.sp.Initialize(self.p1)
        self.sp.SetMinimumPaneSize(10)

        # split h
        self.initpos = 100
        #self.sp.SplitHorizontally(self.p1,self.p2,self.initpos)
        self.sp.SplitVertically(self.p1,self.p2,self.initpos)

class wxWidgetDemo_SplitterApp(wx.App):
    
    #初始化
    def OnInit(self):

        # 创建主窗口
        self.frame = myFrame(parent=None,id = wx.ID_ANY,title = "Splitter Window")
        # 显示主窗口
        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

def main():
    #创建app 对象
    app = wxWidgetDemo_SplitterApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
