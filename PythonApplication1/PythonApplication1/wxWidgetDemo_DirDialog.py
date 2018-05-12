#!/usr/bin/python 
# coding=utf-8


import sys	
import wx
import os


class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        btn = wx.Button(self,label = "选择文件夹")
        self.Bind(wx.EVT_BUTTON,self.onSelDir,btn)

    def onSelDir(self,event):
        dlg = wx.DirDialog(self,message = "选择文件夹",defaultPath=os.getcwd(),style=wx.DD_DEFAULT_STYLE|wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal()==wx.ID_OK:
            print(dlg.GetPath())


class wxWidgetDemo_FileDialogApp(wx.App):
    
    #初始化
    def OnInit(self):

        # 创建主窗口
        self.frame = myFrame(parent=None,id = wx.ID_ANY,title = "DirDialog")
        # 显示主窗口
        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

def main():
    #创建app 对象
    app = wxWidgetDemo_FileDialogApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
