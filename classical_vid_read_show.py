import cv2
import numpy as np
import time
from threading import Thread

cap = cv2.VideoCapture('/boat_amst_AB.mp4')

start = time.time()
frame_count = 0
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  frame_count += 1
  if ret == True:
    # Display the resulting frame
    cv2.imshow('Frame',frame)
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()

end = time.time()
print(f'FPS is {frame_count / (end-start):.2f}')
print(f'Time taken is {(end-start):.2f}second')
