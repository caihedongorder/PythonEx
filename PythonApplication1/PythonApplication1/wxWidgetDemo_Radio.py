#!/usr/bin/python 
# coding=utf-8


import sys	
import wx



class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        panel = wx.Panel(self)

        radio = wx.RadioBox(panel,choices=["男","女","中性"],label = "sex" )

        radio.ShowItem(2,False)
        self.Bind(wx.EVT_RADIOBOX,self.onRadioBox,radio)

    def onRadioBox(self,event):
        print("event type:",type(event))
        print(event.String.encode('gbk'))

        
        pass

class wxWidgetDemo_RadioApp(wx.App):
    
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
    app = wxWidgetDemo_RadioApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
