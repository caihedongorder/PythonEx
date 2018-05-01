#!/usr/bin/python 
# coding=utf-8

import sys	
import wx


class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)
        
        self.panel = wx.Panel(self)

        self.btn = wx.Button(self.panel,label = "测试")

        self.Bind(wx.EVT_BUTTON,self.onClickButton,self.btn)

        self.btn.Bind(wx.EVT_LEFT_DOWN,self.onMouseDown,self.btn)

    def onClickButton(self,event):
        print("改变颜色".decode("utf-8").encode("gbk"))
        self.panel.SetBackgroundColour("green")
        self.panel.Refresh()

    def onMouseDown(self,event):
        self.btn.SetLabel("再一次")
        #为了能让时间继续传递到框架类的onClickButton处理器
        event.Skip()

class wxWidgetDemo_ButtonChangeBGColorApp(wx.App):
    
    #初始化
    def OnInit(self):

        # 创建主窗口
        self.frame = myFrame(parent=None,id = wx.ID_ANY,title = "hello,wxWidget")
        # 显示主窗口
        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

def main():
    #创建app 对象
    app = wxWidgetDemo_ButtonChangeBGColorApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
