#!/usr/bin/python 
# coding=utf-8


import sys	
import wx
import wx.lib.imagebrowser as imagebrowser


class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        btn = wx.Button(self,label = "浏览图片")

        self.Bind(wx.EVT_BUTTON,self.onBrowseImage,btn)

    def onBrowseImage(self,event):
        dlg = imagebrowser.ImageDialog(self)
        if dlg.ShowModal()==wx.ID_OK:
            print(dlg.GetFile())
            


class wxWidgetDemo_ImageBrowserApp(wx.App):
    
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
    app = wxWidgetDemo_ImageBrowserApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
