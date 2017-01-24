import cv2
import numpy as np
import urllib
import os

cam2 = "96.10.1.168"

stream=urllib.urlopen(cam2)
bytes=''
counter = 0
while True:
    
    # to read mjpeg frame -
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
    frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
    # we now have frame stored in frame.

    cv2.imwrite('%-cam2.png' % counter,frame)
    counter = counter + 1
    # Press 'q' to quit 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()