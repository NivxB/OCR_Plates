import cv2
import numpy as np
import urllib
import os

default_url = "http://96.10.1.168/jpg/image.jpg?size=3"

def get_from_livestream(url):
    if url == 0:
        url = default_url
        
    stream=urllib.urlopen(url)
    bytes=''
    while True: 
   	# to read mjpeg frame -
    	bytes+=stream.read(1024)
   	a = bytes.find('\xff\xd8')
    	b = bytes.find('\xff\xd9')
    	if a!=-1 and b!=-1:
        	jpg = bytes[a:b+2]
        	bytes= bytes[b+2:]
    		frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
    		# we now have frame stored in frame.
    		image = np.copy(frame)
    		return image
    

#cv2.destroyAllWindows()
