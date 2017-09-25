#!/usr/bin/python3

from socket import *
from time import ctime

HOST='localhost'
PORT=21567
BUFFSIZ=1024
ADDR=(HOST,PORT)


def SendData(sock,InData):
    sock.send(bytes(InData,'utf-8'))

while True:
    tcpCliSocket=socket(AF_INET,SOCK_STREAM)
    tcpCliSocket.connect(ADDR)
    inputData=input(">>>")
    if not inputData:
        break
    SendData(tcpCliSocket,inputData)
    dataRecv=tcpCliSocket.recv(BUFFSIZ)
    if not dataRecv:
        print("maybe server core dumped!")
        break
    print(dataRecv.decode("utf-8"))
