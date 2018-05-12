#!/usr/bin/python 
# coding=utf-8


import sys	
import wx



class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)

        panel  = wx.Panel(self)

        #self.list = wx.ListBox(panel,choices = [ str(x) for x in range(0,10)],size = (100,100) )
        self.list = wx.CheckListBox(panel,choices = [ str(x) for x in range(0,10)],size = (100,100) )

        self.Bind(wx.EVT_LISTBOX,self.onListBoxChange,self.list)

        self.list.SetSelection(0)

        btn = wx.Button(panel,pos = (100,0),label = "按钮")
        self.Bind(wx.EVT_BUTTON,self.onButton,btn)

    def onListBoxChange(self,event):
        print("onListBoxChange:{select}".format(select = self.list.GetSelection()))

    def onButton(self,event):
        self.list.SetSelection(2)


class wxWidgetDemo_ListApp(wx.App):
    
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
    app = wxWidgetDemo_ListApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
