#!/usr/bin/env python
# coding=utf-8
import os
import sys
import argparse
import subprocess
import re
import Image
import os

parse = argparse.ArgumentParser(description='切割文件')

parse.add_argument('filename',type=str,help='File To Split')
parse.add_argument('--col',default=1,type=int,help='Numbers of Col')
parse.add_argument('--row',default=1,type=int,help='Numbers of Row')

args = parse.parse_args()

print "File To Split",args.filename
print "Numbers of Col",args.col
print "Numbers of Row",args.row

im = Image.open(args.filename)
w,h = im.size
CellWidth = w / args.col
CellHeight = h / args.row

Dir = os.path.dirname(args.filename)
print "OutDir",Dir
BaseName = os.path.basename(args.filename)
Result = BaseName.split('.')
BaseName,extName = Result[0],Result[1]
print "BaseName",BaseName
print "extName",extName

Index = 0
for colIndex in xrange(0,args.col):
    for rowIndex in xrange(0,args.row):
        box = ( rowIndex * CellWidth , colIndex * CellHeight, ( rowIndex+1 ) * CellWidth , ( colIndex+1 ) * CellHeight )
        region = im.crop(box)
        OutFile = os.path.join(Dir,"{0}_{1}.{2}".format(BaseName,Index,extName))
        print "OutDir:{0}".format(OutFile)
        region.save(OutFile)
        Index = Index + 1;
