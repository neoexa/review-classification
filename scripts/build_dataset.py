import pprint 
import csv
import os
import unicodedata
import pandas as pd
import numpy


DATA_REVIEW = "./data/dataset.csv"
DATA_LABEL = "./data/labels.csv"
NEO_DATASET = "./dataset"

df1_colnames = ['review']
df1 = pd.read_csv(DATA_REVIEW, names=df1_colnames, sep='\n', header=None)
df2_colnames = ['label']
df2 = pd.read_csv(DATA_LABEL, names=df2_colnames, sep='\n', header=None)

df = df1.join(df2)

i = 0
while(i < len(df)):
		if (df.iloc[i][1] < 0):
			file_title = NEO_DATASET + "/neg/"+ str(i) + ".txt"
			file=open(file_title, "w+") 
			file.write(''.join(df.iloc[i][0]))
			file.close()
			i+=1
		else:
			file_title = NEO_DATASET + "/pos/"+ str(i) + ".txt"
			file=open(file_title, "w+") 
			file.write(''.join(df.iloc[i][0]))
			file.close()
			i+=1

print("\r" + "DONE. \n")
