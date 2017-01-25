from openalpr import Alpr
import os
import sys
import re
import time

alpr = Alpr("us", "./openalpr.conf", "./runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(3)
#alpr.set_default_region("md")
directory = './Placas'
directoryList = os.listdir(directory)
print(len(directoryList))

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



 # Call when completely done to release memory

alpr.unload()