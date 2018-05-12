#!/usr/bin/python 
# coding=utf-8


import sys	
import wx
import os


class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        btn = wx.Button(self,label = "选择文件")
        self.Bind(wx.EVT_BUTTON,self.onSelFile,btn)

    def onSelFile(self,event):

        #wildcard 格式说明 左边是显示在文件选择对话框 文件类型下拉列表的内容 分别是
        # Python source (*.py) Compiled Python (*.pyc) All files (*.*)
        #   
        wildcard = "Python source (*.py)|*.py|"\
            "Compiled Python (*.pyc)|*.pyc|"\
            "All files (*.*)|*.*"

        dlg = wx.FileSelector("选择文件",default_path=os.getcwd(),wildcard=wildcard)
        if dlg.DoModel() == wx.ID_OK:
            print(dlg.GetPath())
        dlg.Destroy()


class wxWidgetDemo_FileDialogApp(wx.App):
    
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
    app = wxWidgetDemo_FileDialogApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
