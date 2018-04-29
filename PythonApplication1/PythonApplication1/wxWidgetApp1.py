
class $projectname$(object):
    """description of class"""
	pass
	
import wx

#创建 app 对象
app = wx.App()

# 创建主窗口
frame = wx.Frame(None,wx.ID_ANY,"hello,wxWidget")

frame.Show()

#消息循环
app.MainLoop()