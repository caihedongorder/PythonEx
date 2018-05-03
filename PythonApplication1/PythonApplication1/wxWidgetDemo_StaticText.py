#!/usr/bin/python 
# coding=utf-8


import sys	
import wx



class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        panel = wx.Panel(self)

        txt1 = wx.StaticText(panel,label = "static text")

        tst2 = wx.StaticText(panel,label = "static text2",pos=(100,0))
        tst2.SetBackgroundColour("black")
        tst2.SetForegroundColour("red")
        
        tst3 = wx.StaticText(panel,label = "static text3",pos=(200,0),size=(100,100) )
        tst3.SetBackgroundColour("black")
        tst3.SetForegroundColour("red")

        font = wx.Font(30,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
        tst3.SetFont(font)


        
        



        

        

        

class wxWidgetDemo_StaticTextApp(wx.App):
    
    #初始化
    def OnInit(self):

        # 创建主窗口
        self.frame = myFrame(parent=None,id = wx.ID_ANY,title = "hello,StaticText")

        # 显示主窗口
        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

def main():
    #创建app 对象
    app = wxWidgetDemo_StaticTextApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
