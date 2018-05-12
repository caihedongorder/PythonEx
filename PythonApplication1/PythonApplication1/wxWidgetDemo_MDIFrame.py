#!/usr/bin/python 
# coding=utf-8


import sys	
import wx



class myFrame(wx.MDIParentFrame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        menu = wx.Menu()
        id = wx.NewId()
        newItem = menu.Append(id,item='&New')
        
        self.Bind(wx.EVT_MENU,self.onNewFile,newItem)

        menubar = wx.MenuBar()
        menubar.Append(menu,title='&File')

        self.SetMenuBar(menubar)

    def onNewFile(self,event):
        wx.MDIChildFrame(self)
        pass


class wxWidgetDemo_MDIFrameApp(wx.App):
    
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
    app = wxWidgetDemo_MDIFrameApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
