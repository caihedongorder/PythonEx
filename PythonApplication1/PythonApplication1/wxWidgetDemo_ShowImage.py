	
import wx
import sys


class myFrame(wx.Frame):

    def __init__(self,**kwargs):
        #创建图片
        img = wx.Image(name = "images/tiger.jpg")
        bitmap = img.ConvertToBitmap()
        
        size = bitmap.GetWidth(),bitmap.GetHeight()
        #构造基类方法
        super(myFrame, self).__init__(size = size , **kwargs)

        wx.StaticBitmap(parent = self,bitmap = bitmap)

class wxWidgetDemo02App(wx.App):
    
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
    app = wxWidgetDemo02App()
    #消息循环
    app.MainLoop()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
