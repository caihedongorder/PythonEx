#!/usr/bin/python3 
#from socket import *
from socket import *
from time import ctime
HOST = ''
PORT = 21567
BUFFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM);
print('connect to server...')
tcpCliSock.connect(ADDR)

while True:
    data = input('>>>')
    tcpCliSock.send(bytes(data,'utf-8'))
    recvData = tcpCliSock.recv(BUFFSIZE)
    if not recvData:
        print('I Leave')
        break
    print(recvData.decode('utf-8'))

tcpCliSock.close()
