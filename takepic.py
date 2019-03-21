# coding: utf-8

import time
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    
while True:
    starttime = time.time()
    ret, frame = cap.read()
    print('elapse: ', time.time() - starttime)
