	
import wx
import sys

class BlockWindow(wx.Panel):
    """docstring for BlockWindow"""
    def __init__(self,*args,**kwargs):
        super(BlockWindow, self).__init__(*args,**kwargs)
        self.label = '我是BlockWindow'
        self.SetBackgroundColour('red')

        self.Bind(wx.EVT_PAINT,self.onPaint)
    def onPaint(self,event):
        clientSize = self.GetClientRect()
        dc = wx.PaintDC(self)
        fontSizeW,fontSizeH = dc.GetTextExtent(self.label)
        dc.SetFont(self.GetFont())
        dc.DrawText(self.label,(clientSize.width - fontSizeW)*0.5,(clientSize.height-fontSizeH)*0.5)



class myFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)  

        panel = wx.Panel(self)
        sizer = wx.GridSizer(rows=3,cols=3,vgap=5,hgap=5)
        for x in xrange(1,9):
            bw = BlockWindow(panel,size=(100,25))
            sizer.Add(bw,0,0)

        panel.SetSizer(sizer)
        panel.Fit()

class wxWidgetDemoSizer(wx.App):
    #初始化
    def OnInit(self):

        # 创建主窗口
        self.frame = myFrame(parent=None,id = wx.ID_ANY,title = "Sizer 例子")
        # 显示主窗口
        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

def main():
    #创建app 对象
    app = wxWidgetDemoSizer()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
