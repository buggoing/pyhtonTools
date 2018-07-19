#! /usr/bin/python
#coding:utf-8

import hashlib
import os
import sys
import glob
import shutil   
 
def getMD5(file_path):
    md5 = None
    if os.path.isfile(file_path):
        f = open(file_path,'rb')
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
    return md5

def getAllFiles(floder):
    # return os.listdir(floder)    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    return glob.glob(floder + '/*')
    # for rt, dirs, files in os.walk(floder):
    #     for f in files:
    #         print(f)
    #         print(os.path.join(rt, f))

def cpfile(src, dst):
    shutil.copyfile(src, dst)

if __name__ == "__main__":
    floder = sys.argv[1]
    allFiles = getAllFiles(floder)
    newFloder = floder + '_new'
    os.mkdir(newFloder)
    allMD5 = set()
    for fileFullPath in allFiles:
        filemd5 = getMD5(fileFullPath)
        filename = fileFullPath.split('/')[-1]
        print(filename)
        if filemd5 not in allMD5:
            allMD5.add(filemd5)
            cpfile(fileFullPath, os.path.join(newFloder, filename))
