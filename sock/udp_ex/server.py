#!/usr/bin/python3 
#from socket import *
from socket import *
from time import ctime
HOST = ''
PORT = 21567
BUFFSIZE = 1024
ADDR = (HOST,PORT)

tcpSvrSock = socket(AF_INET,SOCK_DGRAM);
tcpSvrSock.bind(ADDR)

while True:
    print('waitting for message...');
    data,addr = tcpSvrSock.recvfrom(BUFFSIZE)
    recvStr=data.decode('utf-8')
    print('recv:',recvStr,addr)
    localstr = ('[%s] %s'%(
            ctime(),recvStr))
    tcpSvrSock.sendto(bytes(localstr,'utf-8'),addr)
