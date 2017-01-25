from openalpr import Alpr
import os
import sys
import re
import time


outFile = open('./data_process_us_modded_2precision.txt','w+')
outFileCSV = open('./data_process_us_modded_2precision.csv','w+')
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
        start_time = time.time()
        results = alpr.recognize_file(directory+'/'+filename)
        start_time = time.time() - start_time
        i += 1
        subI = 0;
        if (len(results['results']) == 0):
         outFile.write("No plate detected on file: %s" % filename)
         outFile.write("\n")
         
         outFileCSV.write("No plate detected on file: %s" % filename)
         outFileCSV.write("\n")
        for plate in results['results']:
            subI += 1; 
            outFile.write("Plate #%s on file: %s" % (str(i)+'.'+str(subI),filename))
            outFile.write('\n')
            outFile.write("Process Time: %s" % (str(start_time)))
            # outFile.write("   ,%12s, %12s" % ("Plate", "Confidence"))
            outFile.write('\n')
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
    else:
        print(filename)
        continue


 # Call when completely done to release memory
outFile.close()
outFileCSV.close()
alpr.unload()