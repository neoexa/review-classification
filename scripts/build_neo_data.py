import pprint 
import csv
import os
import unicodedata
import pandas as pd
import numpy



NEO_DATA = "./neo_data"

df1_colnames = ['review']
df1 = pd.read_csv("data/dataset.csv", names=df1_colnames, sep='\n', header=None)
df2_colnames = ['label']
df2 = pd.read_csv("data/labels.csv", names=df2_colnames, sep='\n', header=None)

df = df1.join(df2)

i = 0
while(i < len(df)):
		if (df.iloc[i][1] < 0):
			file_title = NEO_DATA + "/neg/"+ str(i) + ".txt"
			file=open(file_title, "w+") 
			file.write(''.join(df.iloc[i][0]))
			file.close()
			i+=1
		else:
			file_title = NEO_DATA + "/pos/"+ str(i) + ".txt"
			file=open(file_title, "w+") 
			file.write(''.join(df.iloc[i][0]))
			file.close()
			i+=1

print("\r" + "DONE. \n")
