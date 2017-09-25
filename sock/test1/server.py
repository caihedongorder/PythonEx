#!/usr/bin/python3 
#from socket import *
from socket import *
from time import ctime
HOST = ''
PORT = 21567
BUFFSIZE = 1024
ADDR = (HOST,PORT)

tcpSvrSock = socket(AF_INET,SOCK_STREAM);
tcpSvrSock.bind(ADDR)
tcpSvrSock.listen(5)

while True:
    print('waiting for Connection...')
    tcpCliSock,CliAddr = tcpSvrSock.accept()
    print('...Connected from:',CliAddr)
    while True:
        data = tcpCliSock.recv(BUFFSIZE)
        if not data:
            break
        recvStr=data.decode('utf-8')
        print('recv:',recvStr)
        if recvStr=='ByeBye':
            tcpCliSock.close()
            break
        localstr = ('[%s] %s'%(
            ctime(),recvStr))
        #print(type(localstr))
        tcpCliSock.send(bytes(localstr,'utf-8')) 

tcpSvrSock.close()
