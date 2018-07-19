#! /usr/bin/python
#coding:utf-8

import hashlib
import os
import sys
import glob
import shutil   
import pymysql
from jpegtran import JPEGImage

conn = pymysql.connect(
    host = "192.168.1.12",
    user = "root",
    password = "******",
    database = "******",
    charset = 'utf8',
    cursorclass = pymysql.cursors.DictCursor)
cursor = conn.cursor()

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

def get_image(file_name):
    try:
        image = JPEGImage(file_name).progressive()  #转换成progressive编码
        img_data = image.as_blob()
        if not image:
            logging.error('Get image unavaliable.')
            return None
        format, wid, hei = 'image/jpeg', image.width, image.height
        #将图片划分成9块，crop图片的中心部分并计算md5
        crop_w = wid / 3 + 16 - (wid / 3) % 16
        crop_h = hei / 3 + 16 - (hei / 3) % 16
        crop_img_data = image.crop(crop_w, crop_h, crop_w, crop_h).as_blob()
        crop_md5_code = hashlib.md5(crop_img_data).hexdigest()

        return crop_md5_code
    except Exception as e:
        logging.error('Operate image error with "%s"' %(e))
        return None

def cpfile(src, dst):
    shutil.copyfile(src, dst)

def deduplicate():
    allMD5 = set()
    cursor.execute('select md5 from image where src_src like %s', ['midea%'])
    result = cursor.fetchall()
    for item in result:
        allMD5.add(item['md5'])
    # print(allMD5)
    floder = sys.argv[1]
    allFiles = getAllFiles(floder)
    newFloder = floder + '_new'
    os.mkdir(newFloder)
    count = 0
    for fileFullPath in allFiles:
        filemd5 = get_image(fileFullPath)
        filename = fileFullPath.split('/')[-1]
        if filemd5 not in allMD5:
            print(filename, filemd5)
            count += 1
            allMD5.add(filemd5)
            cpfile(fileFullPath, os.path.join(newFloder, filename))
    print(count)

if __name__ == "__main__":
    deduplicate()