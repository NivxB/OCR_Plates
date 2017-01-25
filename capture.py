from openalpr import Alpr
import numpy as np
import cv2
import os
import sys
import re
import time

cap = cv2.VideoCapture(0)
alpr = Alpr("us", "./openalpr.conf", "./runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(3)
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('Placas',gray)
    cv2.imwrite("Capture.jpg", frame)
    start_time = time.time()
    results = alpr.recognize_file("Capture.jpg")
    start_time = time.time() - start_time
    subI = 0;
    if (len(results['results']) == 0):
        print("No plate detected on file")
        print("\n")
    for plate in results['results']:
        subI += 1; 
        print("Plate detected   ")
        print('\n')
        print("Process Time: %s" % (str(start_time)))
        # print("   ,%12s, %12s" % ("Plate", "Confidence"))
        print('\n')
        for candidate in plate['candidates']:
            prefix = "-"
            if candidate['matches_template']:
                prefix = "*"
            print(" %s %12s %12f" % (prefix, candidate['plate'], candidate['confidence']))
            print('\n')

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

 # Call when completely done to release memory
alpr.unload()  

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()