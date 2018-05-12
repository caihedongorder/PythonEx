#!/usr/bin/python 
# coding=utf-8


import sys	
import wx




class myFrame(wx.Frame):

    def __init__(self,**kwargs):
       
       #构造基类方法
        super(myFrame, self).__init__(**kwargs)


        self.SetWindowStyle( wx.FRAME_SHAPED | wx.SIMPLE_BORDER | wx.FRAME_NO_TASKBAR)


        img = wx.Image(name = "images/tiger1.png")
        bmp = img.ConvertToBitmap()

        clientSize = img.GetWidth(),img.GetHeight()

        self.SetClientSize(img.GetWidth(),img.GetHeight())
        self.SetClientSize(clientSize)

        
        dc = wx.ClientDC(self)
        #dc.DrawBitmap(img.ConvertToBitmap(),0,0)
        dc.DrawBitmap(bmp,0,0,useMask=True)

        r = wx.Region(bmp)
        self.SetShape(r)

        self.bmp = bmp
        self.Bind(wx.EVT_PAINT,self.onPaint)

    def onPaint(self,event):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp,0,0)



class wxWidgetDemo_ShapedWindowApp(wx.App):
    
    #初始化
    def OnInit(self):

        # 创建主窗口
        self.frame = myFrame(parent=None,id = wx.ID_ANY,title = "Shaded Window")
        # 显示主窗口
        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

def main():
    #创建app 对象
    app = wxWidgetDemo_ShapedWindowApp()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
