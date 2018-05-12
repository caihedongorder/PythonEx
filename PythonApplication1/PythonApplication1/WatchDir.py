from watchdog.observers import Observer
from watchdog.events import *
import time
import sys
import os
import traceback
class FileEventHandler(FileSystemEventHandler):
    def __init__(self,path):
        self.path = path
        FileSystemEventHandler.__init__(self)
    '''
    def on_moved(self, event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path,event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path,event.dest_path))
        sys.stdout.flush()

    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))
        sys.stdout.flush()

    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))
        sys.stdout.flush()
    '''
    def on_modified(self, event):
        try:
            if event.src_path.endswith('.py'):
                if not event.is_directory:
                    self.reloadfile(event.src_path)
        except :
            traceback.format_exc()

    def reloadfile(self,fileName):
        #计算模块包路径
        fileName = fileName.replace('\\','/')
        if fileName.startswith(self.path):
            packagePath = fileName[len(self.path)+1:-3]

            packagePath = packagePath.replace('/','.')
            pyMod = __import__(packagePath)
            reload(pyMod)
            print("reload {fileName}".format(fileName = fileName))
            #调用reload方法 重新加载模块
            sys.stdout.flush()

def Start(path):
    observer = Observer()
    event_handler = FileEventHandler(path)
    observer.schedule(event_handler,path,True)
    observer.start()

if __name__ == "__main__":
    try:
        Start(u"H:/ZHUHAI/Content/PythonScripts")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
