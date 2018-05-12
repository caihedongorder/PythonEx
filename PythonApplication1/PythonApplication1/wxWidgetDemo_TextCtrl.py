#!/usr/bin/python 
# coding=utf-8


import sys	
import wx



class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        panel = wx.Panel(self)

        wx.StaticText(panel,label = "Multi-line",pos=(0,0))

        wx.TextCtrl(panel,pos=(100,0),size=(100,100),style=wx.TE_MULTILINE)


        wx.StaticText(panel,label="Rich Text",pos=(0,120))
        
        richText = wx.TextCtrl(panel,pos=(100,120),size=(100,100),style=wx.TE_MULTILINE | wx.TE_RICH2 , 
                               value = "Rich Text")
        richText.SetStyle(44,52,wx.TextAttr("White","Black"))


        

class wxWidgetDemo_TextCtrlApp(wx.App):
    
    #初始化
    def OnInit(self):

        # 创建主窗口
        self.frame = myFrame(parent=None,id = wx.ID_ANY,title = "hello,TextCtrl")
        # 显示主窗口
        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

def main():
    #创建app 对象
    app = wxWidgetDemo_TextCtrlApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
