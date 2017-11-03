#!/usr/bin/env python    
# encoding: utf-8
import sys 
from PIL import Image
import cv2

def main(filename)

  img = cv2.imread(filename)
  grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  cv2.imwrite('gray-' + filename, grayImg)
  cv2.imshow('gray', grayImg)
  
  # img = Image.open(filename)
  # grayImg = img.convert('L')


main(sys.argv[1])
# loadDataFromFile('3-data.json')