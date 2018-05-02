#!/usr/bin/python 
# coding=utf-8


import sys	
import wx



class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)
        
        self.createMenuBar()

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        self.SetMenuBar(menuBar)
        for menuLabel,menuItems in self.menuData() :
            print(menuLabel)
            print(menuItems)
            menuBar.Append(self.createMenu(menuItems),menuLabel)

    def createMenu(self,InMenuItems):
        menu = wx.Menu()
        #for label,helpString,callback,kindId in InMenuItems:
        for item in InMenuItems:
            if len(item) != 2:
                label,helpString,callback,kindId = item
                if label == "":
                    menu.AppendSeparator()
                else:
                    menu.Append(wx.NewId(),item = label,helpString = helpString,kind = kindId)
            else:
                label,subMenuItems = item
                subMenu = self.createMenu(subMenuItems)
                menu.AppendMenu(wx.NewId(),label,subMenu)
        return menu

    def menuData(self):
        return [(
                #文件菜单
                "&File",[
                    ("&New","New file",self.onNewFile , wx.ITEM_NORMAL),
                    ("&Open","Open file",self.onOpenFile , wx.ITEM_NORMAL),
                    ("&Save","Save file",self.onOpenFile , wx.ITEM_NORMAL),
                    ("","","",wx.ITEM_NORMAL),
                    ("&Color",(
                            ("&Black","",self.onColor, wx.ITEM_RADIO),
                            ("&Red","",self.onColor, wx.ITEM_RADIO),
                            ("&Green","",self.onColor, wx.ITEM_RADIO),
                            ("&Blue","",self.onColor, wx.ITEM_RADIO),
                        )),
                    ("","","",wx.ITEM_NORMAL),
                    ("&Quit","Quit",self.onCloseWindow , wx.ITEM_NORMAL),
                    ]
                )]
    def onNewFile(self,event):
        pass
    def onOpenFile(self,event):
        pass
    def onSaveFile(self,event):
        pass
    def onColor(self,event):
        pass
    def onCloseWindow(self,event):
        pass

class wxWidgetDemo_MenuApp(wx.App):
    
    #初始化
    def OnInit(self):

        # 创建主窗口
        self.frame = myFrame(parent=None,id = wx.ID_ANY,title = "菜单展示")
        # 显示主窗口
        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

def main():
    #创建app 对象
    app = wxWidgetDemo_MenuApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
