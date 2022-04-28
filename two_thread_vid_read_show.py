# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:17:21 2022

@author: talha
"""

import cv2
import numpy as np
import time
from threading import Thread
p = 'C:/Users/talha/Downloads/Compressed/VSQAD/Reference videos/boat_amst_AB.mp4'
def process(img):
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.putText(img, "Text", (220, 450), cv2.FONT_HERSHEY_SIMPLEX, 10.0, (0, 0, 255)) 
    return img
class VidRead:
    def __init__(self, src):
        self.cap = cv2.VideoCapture(src)
        (self.ret, self.frame) = self.cap.read()
        self.stop_read = False
    
    def count_frames(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    def vid_reader(self):
        while not self.stop_read:
            if self.ret == False:
                self.stop()
            else:
                (self.ret, self.frame) = self.cap.read()

    def stop(self):
        self.stop_read = True
        #self.vid_thread.join()
        
    def start_thread(self):
        self.vid_thread = Thread(target=self.vid_reader, args=())
        self.vid_thread.start()
        return self
    
class VidShow:
    def __init__(self, frame):
        self.frame = frame
        self.stop_show = False
        
    def start_show(self):
        while not self.stop_show:
            self.frame = process(self.frame)
            cv2.imshow('Frame', self.frame)
            if cv2.waitKey(1) == ord("q"):
                self.stop_show = True

    def stop(self):
        self.stop_show = True
        self.show_thread.join()
    
    def start_thread(self):
        self.show_thread = Thread(target=self.start_show, args=())
        self.show_thread.start()
        return self
        
start = time.time()
frame_count = 0

vid = VidRead(p).start_thread()
show = VidShow(vid.frame).start_thread()

total_frames = vid.count_frames()

while True:

    vid_frame = vid.frame
    show.frame = vid_frame

    frame_count += 1
    if (cv2.waitKey(1) == ord("q")) or vid.stop_read or show.stop_show:
        vid.stop()
        show.stop()
        cv2.destroyAllWindows()
        break
    
cv2.destroyAllWindows() 


end = time.time()
print(f'FPS is {frame_count / (end-start):.2f}')
print(f'Time taken is {(end-start):.2f}second')
