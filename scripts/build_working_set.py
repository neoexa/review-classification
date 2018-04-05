import re
import os, errno
import sys
import csv
import random
import string
import sys
import time

import pandas as pd

filePath = "./working_set"

df = pd.read_csv("./original_dirty_data/dataset.csv", sep='\n')


# à refaire !!!
i=0
while(i<4999):
	outfile = filePath + "/neg/"+ str(i) + ".txt"
	file=open(outfile, "w+") 
	file.write(''.join(df.iloc[i][0]))
	file.close()
	i = i+1
while(i<9999):
	outfile = filePath + "/pos/"+ str(i) + ".txt"
	file=open(outfile, "w+") 
	file.write(''.join(df.iloc[i][0]))
	file.close()
	i = i+1
sys.stdout.write("\r" + "DONE. \n")
sys.stdout.flush()