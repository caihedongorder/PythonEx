#!/usr/bin/python 
# coding=utf-8


import sys	
import wx

#定义事件
class TowButtonEvent(wx.CommandEvent):
    def __init__(self, *args):
        self.__clickCount = 0
        return super(TowButtonEvent, self).__init__(*args)
    @property
    def clickCount(self):
        return self.__clickCount
    @clickCount.setter
    def clickCount(self,InClickCount):
        self.__clickCount = InClickCount

#创建事件绑定器
myEVT_TWO_BUTTON = wx.NewEventType()
EVT_TOW_BUTTON = wx.PyEventBinder( myEVT_TWO_BUTTON ,1)



class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        self.buttonClickCount = 0
        self.isLeftButtonClick = False
        self.isRightButtonClick = False

        btn1 = wx.Button(self,label = "左按钮")
        btn2 = wx.Button(self,label = "右按钮",pos = (100,0))
        

        self.Bind(wx.EVT_BUTTON,self.onClickLeftBtn,btn1)
        self.Bind(wx.EVT_BUTTON,self.onClickRightBtn,btn2)

    #左按键点击
    def onClickLeftBtn(self,event):
        self.isLeftButtonClick = True
        self.onClick()
        event.Skip()
    #右按键点击
    def onClickRightBtn(self,event):
        self.isRightButtonClick = True
        self.onClick()
        event.Skip()

    def onClick(self):
        self.buttonClickCount +=1
        if self.isLeftButtonClick and self.isRightButtonClick:
            self.isLeftButtonClick = False
            self.isRightButtonClick = False

            #处理自定义事件
            print("自定义事件 点击次数:{clickCount}".format(clickCount = self.buttonClickCount).decode("utf-8").encode("gbk"))

            evt = TowButtonEvent( myEVT_TWO_BUTTON,self.GetId())
            evt.clickCount = self.buttonClickCount
            self.GetEventHandler().ProcessEvent(evt)


class wxWidgetDemo_CustumEventApp(wx.App):
    
    #初始化
    def OnInit(self):

        # 创建主窗口
        self.frame = myFrame(parent=None,id = wx.ID_ANY,title = "hello,wxWidget")
        # 显示主窗口
        self.frame.Show()

        self.SetTopWindow(self.frame)

        self.Bind(EVT_TOW_BUTTON,self.OnTwoButtonEvent)

        return True

    def OnTwoButtonEvent(self,event):
        self.frame.SetTitle("Click Count:{clickCount}".format(clickCount = event.clickCount))

def main():
    #创建app 对象
    app = wxWidgetDemo_CustumEventApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
