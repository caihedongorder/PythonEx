#!/usr/bin/env python
# coding=utf-8
import os
import sys
import argparse

parse = argparse.ArgumentParser(description='Use to Count File Line Count')

parse.add_argument('--ext',nargs='*',type=str,help='需要统计的文件后缀名')
parse.add_argument('--r',action = 'store_true',help='是否遍历文件夹')

args = parse.parse_args()

try:
    if len(args.ext)==0:
        sys.exit('未指定需要统计的文件后缀名')
except:
    sys.exit('未指定需要统计的文件后缀名')
    
exts = args.ext
curdir = os.curdir

target_files = []

def find_all_target_files(InDir,bRescurse):
    for file in os.listdir(InDir):
        subpath = os.path.join(InDir,file)
        if os.path.isfile(subpath):
            base,ext = os.path.splitext(subpath)
            if ext[1:] in exts:
                target_files.append(subpath)
        else:
            if os.path.isdir(subpath) and bRescurse:
                # print('enter path:'+ subpath)
                find_all_target_files(subpath,bRescurse)


find_all_target_files(curdir,True)

for file in target_files:
    print(file+" is target files")



