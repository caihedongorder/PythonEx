#!/usr/bin/python3

from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

HOST=''
PORT=21567
ADDR=(HOST,PORT)

def string2bytes(InString,InEncoding='utf-8'):
    return bytes(InString,InEncoding)

class MyRequestHandler(SRH):
    def handle(self):
        print("...connected from:",self.client_address)
        self.wfile.write(string2bytes('welcome!'))

tcpServ = TCP(ADDR,MyRequestHandler)
print("waitting for connection...")
tcpServ.serve_forever()
