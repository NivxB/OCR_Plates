from openalpr import Alpr
import os
import sys
import re
import time
import datetime
import demo_livestream
import process_image

outFile = open('./data_process_us_modded_livestream.txt','w+')
outFileCSV = open('./data_process_us_modded_livestream.csv','w+')
alpr = Alpr("us", "./openalpr.conf", "./runtime_data")
if not alpr.is_loaded():
    outFile.write("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(3)
while True:
    start_time = time.time()
    start_time = datetime.datetime.fromtimestamp(start_time)
    image = demo_livestream.get_from_livestream(0)
    results = alpr.recognize_array(image.tobytes())
    if (len(results['results']) == 0):
        outFile.write("No plate detected on file: %s" % str(start_time))
        outFile.write("\n")
    for plate in results['results']:
        outFile.write("Plate on time: %s" % str(start_time))
        outFile.write('\n')
        # outFile.write("   ,%12s, %12s" % ("Plate", "Confidence"))
        for candidate in plate['candidates']:
            prefix = "-"
            if candidate['matches_template']:
                prefix = "*"
                outFile.write(" %s %12s %12f" % (prefix, candidate['plate'], candidate['confidence']))
                outFile.write('\n')
                ##CSV
                outFileCSV.write("%s,%f" % (candidate['plate'], candidate['confidence']))
                outFileCSV.write('\n')
        continue
    time.sleep(2)
