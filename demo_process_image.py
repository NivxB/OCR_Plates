from openalpr import Alpr
import os
import process_image
import sys
import re
import time


outFile = open('./data_process_us_modded_2precision.txt','w+')
alpr = Alpr("us", "./openalpr.conf", "./runtime_data")
if not alpr.is_loaded():
    outFile.write("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(3)
#alpr.set_default_region("md")
directory = './Placas'
directoryList = os.listdir(directory)
print(len(directoryList))
i = 0
for filename in directoryList:
    if filename.endswith(".jpg") or filename.endswith(".png"): 
        process_image.main_process(directory+'/'+filename)
        continue
    else:
        print(filename)
        continue


 # Call when completely done to release memory
outFile.close()
alpr.unload()