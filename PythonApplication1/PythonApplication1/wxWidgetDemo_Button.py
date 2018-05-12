#!/usr/bin/python 
# coding=utf-8


import sys	
import wx

import wx.lib.buttons as wxButtons



class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        panel = wx.Panel(self)

        wx.Button(panel,pos = (0,0) , label  = "button 1")
        wx.ToggleButton(panel,pos = (0,40) , label  = "button 2")
        
        img = wx.Image("images/tiger.jpg")
        bmp = img.ConvertToBitmap()
        wx.BitmapButton(panel,pos = (0,80) , bitmap = bmp ,size=(100,30))

        #wxButtons.GenBitmapTextToggleButton(panel,pos = (0,120),bitmap = img.ConvertToBitmap() , size = (100,30))


class wxWidgetDemo_ButtonApp(wx.App):
    
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
    app = wxWidgetDemo_ButtonApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
