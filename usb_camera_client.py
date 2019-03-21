# coding: utf-8

import Queue
import time
import threading
import cv2

QUEUE_SIZE = 10
TIME_INTERVAL_TAKE_PHOTO = 0.03 # camera is 30 FPS

class CameraClient():
    def __init__(self, camNo = 0):
        cap = cv2.VideoCapture(camNo)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        self.cap = cap
        self.photoQueue = Queue.Queue(maxsize=QUEUE_SIZE)
        self.th = threading.Thread(target=self._takePhotoWorker)
        self.th.setDaemon(True)
        self.th.start()


    def _takePhotoWorker(self):
        while True:
            
            ret, frame = self.cap.read()
            if ret:
                if self.photoQueue.full():
                    self.photoQueue.get()
                self.photoQueue.put(frame)

            time.sleep(TIME_INTERVAL_TAKE_PHOTO)
    
    def getPhoto(self):
        return self.photoQueue.get()

