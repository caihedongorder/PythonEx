#!/usr/bin/python3 
#from socket import *
from socket import *
from time import ctime
HOST = 'localhost'
PORT = 21567
BUFFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_DGRAM);

while True:
    sendData = input('>>>')
    tcpCliSock.sendto(bytes(sendData,'utf-8'),ADDR)
    recvData = tcpCliSock.recvfrom(BUFFSIZE)
    print('recv message:',recvData) 
