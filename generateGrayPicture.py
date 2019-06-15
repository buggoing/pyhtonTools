#!/usr/bin/env python    
# encoding: utf-8
import sys
import os
from PIL import Image
import cv2

def main(filepath):
  basename = os.path.basename(filepath)
  dirname = os.path.dirname(filepath)
  img = cv2.imread(filepath)
  grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # grayImg = img.convert('L')
  newFileName = 'grey_' + basename
  newFilepath = os.path.join(dirname, newFileName)
  print(newFileName, newFilepath)
  cv2.imwrite(newFilepath, grayImg)
  cv2.imshow('gray', grayImg)
  
  # img = Image.open(filename)
  # grayImg = img.convert('L')


main(sys.argv[1])
# loadDataFromFile('3-data.json')