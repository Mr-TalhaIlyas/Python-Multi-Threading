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

    def vid_reader(self):
        while not self.stop_read:
            (self.ret, self.frame) = self.cap.read()
    def stop(self):
        self.stop_read = True
    
    def start_thread(self):
        Thread(target=self.vid_reader, args=()).start()
        return self

start = time.time()
frame_count = 0
vid = VidRead(p).start_thread()

while True:
    vid_frame = vid.frame
    #print(vid_frame)
    if vid.ret == True:
        
        vid_frame = process(vid_frame)
        
        cv2.imshow('Frame', vid_frame)
        
        frame_count += 1
        
        if (cv2.waitKey(1) == ord("q")) or vid.stop_read:
            vid.stop()
            break
    else:
        break
    
cv2.destroyAllWindows() 
end = time.time()
print(f'FPS is {frame_count / (end-start):.2f}')
print(f'Time taken is {(end-start):.2f}second')
