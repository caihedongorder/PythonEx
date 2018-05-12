#!/usr/bin/python 
# coding=utf-8


import sys	
import wx



class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        panel = wx.Panel(self)

        wx.Slider(panel,value = 10,size = (300,20),style=wx.SL_LABELS|wx.SL_HORIZONTAL)


        wx.Slider(panel,value = 10,pos = (150,50),size = (20,300),style=wx.SL_LABELS|wx.SL_VERTICAL)


class wxWidgetDemo_SliderApp(wx.App):
    
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
    app = wxWidgetDemo_SliderApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
